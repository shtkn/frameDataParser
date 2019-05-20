import unittest
from parseAttacks import *


class TestParseAttackMethods(unittest.TestCase):
    def test_combine_2_wait_frames(self):
        chunks = [WaitFrameChunk(2), WaitFrameChunk(4)]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrameChunk(6)]
        self.assertItemsEqual(result, expected)

    def test_combine_2_active_frames(self):
        chunks = [AttackFrameChunk(2), AttackFrameChunk(2, is_new_hit=False)]
        result = consolidate_frame_chunks(chunks)
        expected = [AttackFrameChunk(4)]
        self.assertItemsEqual(result, expected)

    def test_dont_combine_2_active_frames(self):
        chunks = [AttackFrameChunk(2, is_new_hit=True), AttackFrameChunk(2, is_new_hit=True)]
        result = consolidate_frame_chunks(chunks)
        expected = [AttackFrameChunk(2), AttackFrameChunk(2)]
        self.assertItemsEqual(result, expected)

    def test_combine_2_wait_frames_with_active_after(self):
        chunks = [WaitFrameChunk(2), WaitFrameChunk(4), AttackFrameChunk(1), WaitFrameChunk(2)]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrameChunk(6), AttackFrameChunk(1), WaitFrameChunk(2)]
        self.assertItemsEqual(result, expected)

    def test_get_duration(self):
        self.assertEqual(15, get_duration("    sprite('null', 15)"))

    def test_simulate_hit_basic_normal(self):
        chunks = [WaitFrameChunk(4), AttackFrameChunk(1, 4, 4), WaitFrameChunk(12),
                  AttackFrameChunk(1, 4, 4), WaitFrameChunk(12)]
        move = Move()
        move.frame_chunks = chunks
        # no effects to combine, just expect teh same chunks back
        result = combine_with_effects_on_block(move, {})
        self.assertEqual(0, len(result.additional_chunks))
        self.assertItemsEqual(move.frame_chunks, chunks)

    def test_simulate_hit_projectile(self):
        chunks = [WaitFrameChunk(4), SubroutineCall("Shot"), WaitFrameChunk(12)]
        shot = Move()
        shot.frame_chunks = [WaitFrameChunk(4), AttackFrameChunk(2)]
        effect_list = {"Shot": shot}
        move = Move()
        move.frame_chunks = chunks
        # combine with ShotAnimation
        result = combine_with_effects_on_block(move, effect_list)
        self.assertEqual(1, len(result.additional_chunks))
        self.assertItemsEqual(result.frame_chunks, [WaitFrameChunk(16)])
        # basically increasing the startup of hte shot by 4
        self.assertItemsEqual(result.additional_chunks[0], [WaitFrameChunk(8), AttackFrameChunk(2)])

    def test_simulate_hit_use_subroutine(self):
        chunks = [WaitFrameChunk(4), SubroutineCall("InitValues"), AttackFrameChunk(1, 10, 11, 12), WaitFrameChunk(4)]
        init = Subroutine()
        init.hitstop = 1
        init.blockstun = 2
        init.additionalHitstopOpponent = 3
        init.landingRecovery = 4
        effect_list = {"InitValues": init}
        move = Move()
        move.frame_chunks = chunks
        move.landing_recovery = 100
        result = combine_with_effects_on_block(move, effect_list)
        # expect hitstop, blockstun, landing recovery etc to be replaced by values from InitValues
        self.assertEqual(0, len(result.additional_chunks))
        expected_frame_chunks = [WaitFrameChunk(4),
                                 AttackFrameChunk(1, init.blockstun, init.hitstop, init.additionalHitstopOpponent),
                                 WaitFrameChunk(4)]
        self.assertItemsEqual(result.frame_chunks, expected_frame_chunks)
        self.assertEqual(init.landingRecovery, result.landing_recovery)

    def test_simulate_projectile_using_subroutine(self):
        chunks = [WaitFrameChunk(4), SubroutineCall("Shot"), WaitFrameChunk(12)]
        shot = Move()
        shot.frame_chunks = [SubroutineCall("ShotInit"), WaitFrameChunk(4), AttackFrameChunk(2)]
        shot_init = Subroutine()
        shot_init.hitstop = 1
        shot_init.blockstun = 2
        shot_init.additionalHitstopOpponent = 3
        effect_list = {"Shot": shot,
                       "ShotInit": shot_init}
        move = Move()
        move.frame_chunks = chunks
        # combine with ShotAnimation
        result = combine_with_effects_on_block(move, effect_list)
        self.assertEqual(1, len(result.additional_chunks))
        self.assertItemsEqual(result.frame_chunks, [WaitFrameChunk(16)])
        # basically increasing the startup of hte shot by 4
        expected_frame_chunks = [WaitFrameChunk(8),
                                 AttackFrameChunk(2,
                                                  shot_init.blockstun,
                                                  shot_init.hitstop,
                                                  shot_init.additionalHitstopOpponent
                                                  )
                                 ]
        self.assertItemsEqual(result.additional_chunks[0], expected_frame_chunks)

