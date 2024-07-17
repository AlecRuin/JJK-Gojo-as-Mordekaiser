#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Mordekaiser/Animations/Skin0" = AnimationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Attack2" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xc509f8e4 = ParticleEventData {
                        mEffectKey: hash = 0x7d9faa7d
                        mStartFrame: f32 = 11
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                    }
                    0x1e14ea15 = StopAnimationEventData {
                        mEndFrame: f32 = 30
                        mStopAnimationName: hash = 0xf301e808
                    }
                    0x373e9c78 = StopAnimationEventData {
                        mEndFrame: f32 = 30
                        mStopAnimationName: hash = 0x9204de61
                    }
                    0x14f890d7 = StopAnimationEventData {
                        mEndFrame: f32 = 30
                        mStopAnimationName: hash = 0x8dd8b42e
                    }
                    0x7470e324 = StopAnimationEventData {
                        mEndFrame: f32 = 30
                        mStopAnimationName: hash = 0x7470e324
                    }
                    0x5ab4742c = StopAnimationEventData {
                        mEndFrame: f32 = 30
                        mStopAnimationName: hash = 0x46c1234b
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/AutoAttack2.anm"
                }
            }
            "Channel_Loop" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x1cb8d2a4 = SubmeshVisibilityEventData {}
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Channel.anm"
                }
            }
            "Channel_Wndup" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Channel_WNDUP.anm"
                }
            }
            "Crit" = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Attack_Turret.anm"
                }
            }
            "Death" = AtomicClipData {
                mTrackDataName: hash = "Death"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Death" = SoundEventData {
                        mSoundName: string = "Play_sfx_Mordekaiser_Death3D"
                        mIsLoop: bool = false
                    }
                    0xdf05b562 = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_Death"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                    }
                    "Hide" = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "mAce"
                        }
                        mHideSubmeshList: list[hash] = {
                            "HEAD"
                            0xc1abfc9e
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Death.anm"
                }
            }
            0xe624fd89 = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Idle.anm"
                }
            }
            0xe324f8d0 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Idle.anm"
                }
            }
            0xe424fa63 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Idle.anm"
                }
            }
            "Laugh" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x0cf0606b = SoundEventData {
                        mSoundName: string = "Play_sfx_Mordekaiser_Laugh_cast"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Mordekaiser_Laugh.anm"
                }
            }
            "Spell1" = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "mAce" = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_Q_Mace"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsKillEvent: bool = false
                        mScalePlaySpeedWithAnimation: bool = true
                    }
                    "Mace_Charge" = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_Q_Mace_Charge"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x76720700
                            }
                        }
                    }
                    0x248d2859 = ParticleEventData {
                        mEffectKey: hash = 0x293db49e
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x18dacb1c
                            }
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell_1.anm"
                }
            }
            "Spell4" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x711e7aa2 = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_R_Mace"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    "Mordekaiser_R_Blackhole_Vfx"= ParticleEventData{
                        mEffectKey: hash = "Mordekaiser_R_Blackhole"
                        mStartFrame: f32 = 11
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                    }
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                    0x7be7fe3d = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_R_Mace_Head"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x76720700
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell_4_cast.anm"
                }
            }
            "Taunt" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Taunt" = SoundEventData {
                        mSoundName: string = "Play_sfx_Mordekaiser_Taunt_cast"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Taunt.anm"
                }
            }
            0xf53bbfdb = AtomicClipData {
                mMaskDataName: hash = 0x432b1d96
                mTrackDataName: hash = 0x432b1d96
                mEventDataMap: map[hash,pointer] = {
                    "WeaponSnap" = JointSnapEventData {
                        mName: hash = "WeaponSnap"
                        mJointNameToOverride: hash = "weapon"
                        mJointNameToSnapTo: hash = 0xf5a0e258
                    }
                    0xa5db086f = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_E_HandGlow"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xe3da48b0
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x1a606980 = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_E_Cast_Ground"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                    }
                }
                mTickDuration: f32 = 0.0322580636
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell2_Cast.anm"
                }
            }
            "Recall" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0x9ef392c9
                }
            }
            0x7d925843 = AtomicClipData {
                mTrackDataName: hash = "TURN"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Turns_Left_90.anm"
                }
            }
            0x3a37e619 = AtomicClipData {
                mTrackDataName: hash = "TURN"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Turn_Right_90.anm"
                }
            }
            "Turn_0" = AtomicClipData {
                mTrackDataName: hash = "TURN"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Turn_0.anm"
                }
            }
            "TURN" = ParametricClipData {
                mTrackDataName: hash = "TURN"
                Updater: pointer = 0x564d2410 {}
                mParametricPairDataList: list[embed] = {
                    ParametricPairData {
                        mClipName: hash = 0x7d925843
                        mValue: f32 = -70
                    }
                    ParametricPairData {
                        mClipName: hash = "Turn_0"
                    }
                    ParametricPairData {
                        mClipName: hash = 0x3a37e619
                        mValue: f32 = 70
                    }
                }
            }
            "Idle_In" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Idle_In.anm"
                }
            }
            "Homeguard" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mTickDuration: f32 = 0.0666666701
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Run.anm"
                }
            }
            "Run_Homeguard" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x643a01ca = ConformToPathEventData {
                        mMaskDataName: hash = 0x643a01ca
                        mBlendInTime: f32 = 0.150000006
                        mBlendOutTime: f32 = 0.150000006
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Run.anm"
                }
            }
            "Walk" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xed66d676 = ConformToPathEventData {
                        mMaskDataName: hash = 0x643a01ca
                        mBlendInTime: f32 = 0.150000006
                        mBlendOutTime: f32 = 0.150000006
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Walk.anm"
                }
            }
            "Run" = ConditionFloatClipData {
                mFlags: u32 = 2
                mConditionFloatPairDataList: list[embed] = {
                    ConditionFloatPairData {
                        mClipName: hash = "Walk"
                        mValue: f32 = 400
                    }
                    ConditionFloatPairData {
                        mClipName: hash = "Run_Homeguard"
                        mValue: f32 = 401
                    }
                }
                Updater: pointer = 0x3c38f0fa {}
                mChangeAnimationMidPlay: bool = true
                mChildAnimDelaySwitchTime: f32 = 0.200000003
            }
            0x700fcd2f = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = 0x432b1d96
                mEventDataMap: map[hash,pointer] = {
                    0x1a606980 = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_E_Cast_Ground"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0xa5db086f = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_E_HandGlow"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xe3da48b0
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "mAce"
                        mJointNameToSnapTo: hash = 0xfc1254bb
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell3_Cast.anm"
                }
            }
            "Spell1_To_Idle" = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "StopTurn"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell_1_to_Idle.anm"
                }
            }
            0xa24eb64e = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell_1_torun_0.anm"
                }
            }
            0xf5d7ef7b = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell_1_torun_90.anm"
                }
            }
            0x24906eec = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell_1_torun_-90.anm"
                }
            }
            0x3498eb31 = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {}
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell_1_torun_180.anm"
                }
            }
            0x0376e134 = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell_1_torun_-180.anm"
                }
            }
            "Spell1_ToRun" = ParametricClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                Updater: pointer = 0x41356ce8 {}
                mParametricPairDataList: list[embed] = {
                    ParametricPairData {
                        mClipName: hash = 0x0376e134
                        mValue: f32 = -179
                    }
                    ParametricPairData {
                        mClipName: hash = 0x24906eec
                        mValue: f32 = -90
                    }
                    ParametricPairData {
                        mClipName: hash = 0xa24eb64e
                    }
                    ParametricPairData {
                        mClipName: hash = 0xf5d7ef7b
                        mValue: f32 = 90
                    }
                    ParametricPairData {
                        mClipName: hash = 0x3498eb31
                        mValue: f32 = 179
                    }
                }
            }
            "Spell2_Idle" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xf3745acb = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "R_Hand"
                        mJointNameToSnapTo: hash = 0xa09830a0
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell2_Idle.anm"
                }
            }
            0x63585ed3 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = 0x0a70dc21
                mEventDataMap: map[hash,pointer] = {
                    0x4ae08392 = SoundEventData {
                        mSoundName: string = "Play_sfx_Mordekaiser_walk"
                        mIsKillEvent: bool = false
                    }
                    0x49e081ff = SoundEventData {
                        mStartFrame: f32 = 17
                        mSoundName: string = "Play_sfx_Mordekaiser_walk"
                        mIsKillEvent: bool = false
                    }
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                    0xa979a542 = ParticleEventData {
                        mStartFrame: f32 = 3
                        mEffectKey: hash = "Mordekaiser_W_footstep"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x235c7745
                            }
                        }
                    }
                    0x14afdbac = ParticleEventData {
                        mStartFrame: f32 = 19
                        mEffectKey: hash = "Mordekaiser_W_footstep"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x215c93e3
                            }
                        }
                    }
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "mAce"
                        mJointNameToSnapTo: hash = 0xfc1254bb
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell2_Walk.anm"
                }
            }
            0x46c1234b = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mMaskDataName: hash = 0x432b1d96
                mTrackDataName: hash = 0x432b1d96
                mEventDataMap: map[hash,pointer] = {
                    0xc732ff85 = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "mAce"
                        mJointNameToSnapTo: hash = 0xfc1254bb
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell2_Intro_Upper_Walk.anm"
                }
            }
            0xeb3f8435 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell4_Move.anm"
                }
            }
            0x2a91aa32 = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x875c32d5 = SoundEventData {
                        mSoundName: string = "Play_sfx_Mordekaiser_W_foley_end"
                        mIsLoop: bool = false
                    }
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "R_Hand"
                        mJointNameToSnapTo: hash = 0xa09830a0
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell2_Outro.anm"
                }
            }
            0x9204de61 = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mMaskDataName: hash = 0x432b1d96
                mTrackDataName: hash = 0x432b1d96
                mEventDataMap: map[hash,pointer] = {
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "R_Hand"
                        mJointNameToSnapTo: hash = 0xa09830a0
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell2_Run_Exit.anm"
                }
            }
            0xf301e808 = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xc732ff85 = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "mAce"
                        mJointNameToSnapTo: hash = 0xfc1254bb
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell2_Intro.anm"
                }
            }
            0x7470e324 = ConditionBoolClipData {
                Updater: pointer = 0x6c816d62 {}
                mChangeAnimationMidPlay: bool = true
                mTrueConditionClipName: hash = 0x46c1234b
                mFalseConditionClipName: hash = 0xf301e808
            }
            0x93cc45d2 = ConditionBoolClipData {
                Updater: pointer = 0x6c816d62 {}
                mChangeAnimationMidPlay: bool = true
                mTrueConditionClipName: hash = 0x9204de61
                mFalseConditionClipName: hash = 0x2a91aa32
            }
            0x9c3ecd25 = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mMaskDataName: hash = 0x432b1d96
                mTrackDataName: hash = 0x432b1d96
                mEventDataMap: map[hash,pointer] = {
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "R_Hand"
                        mJointNameToSnapTo: hash = 0xa09830a0
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell2_Run_Sheild_Consume_Exit.anm"
                }
            }
            0x8dd8b42e = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "R_Hand"
                        mJointNameToSnapTo: hash = 0xa09830a0
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell2_Consume_Shield.anm"
                }
            }
            0xe612766e = ConditionBoolClipData {
                Updater: pointer = 0x6c816d62 {}
                mChangeAnimationMidPlay: bool = true
                mTrueConditionClipName: hash = 0x9c3ecd25
                mFalseConditionClipName: hash = 0x8dd8b42e
            }
            "Spell2_Idle_In" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xc732ff85 = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "R_Hand"
                        mJointNameToSnapTo: hash = 0xa09830a0
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell2_Idle_In.anm"
                }
            }
            0xde27ecc4 = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mMaskDataName: hash = 0x432b1d96
                mTrackDataName: hash = 0x432b1d96
                mEventDataMap: map[hash,pointer] = {
                    0x76c40efc = JointSnapEventData {
                        mJointNameToOverride: hash = "mAce"
                        mJointNameToSnapTo: hash = 0xfc1254bb
                    }
                    0xa5db086f = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_E_HandGlow"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xe3da48b0
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x1a606980 = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_E_Cast_Ground"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell3_Cast_Walk.anm"
                }
            }
            0xc0439cdd = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xc732ff85 = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Battle_Idle_to_Idle.anm"
                }
            }
            "Idle_Selector" = SelectorClipData {
                mFlags: u32 = 2
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = 0xe624fd89
                        mProbability: f32 = 0.330000013
                    }
                    SelectorPairData {
                        mClipName: hash = 0xe324f8d0
                        mProbability: f32 = 0.330000013
                    }
                    SelectorPairData {
                        mClipName: hash = 0xe424fa63
                        mProbability: f32 = 0.340000004
                    }
                }
            }
            "Idle1" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Battle_Idle"
                    0xc0439cdd
                    "Idle_Selector"
                }
            }
            "Battle_Idle" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Battle_Idle_1.anm"
                }
            }
            "Passive" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Passive.anm"
                }
            }
            0x9f98b829 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell1_to_Attack.anm"
                }
            }
            0x9ef392c9 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x570cdcd7 = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_Recall_Stairs"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                    }
                    "Audio_Recall" = SoundEventData {
                        mSoundName: string = "Play_sfx_Mordekaiser_Recall_cast"
                        mIsLoop: bool = false
                    }
                    "FaceCamera" = 0xd7a6b107 {}
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/recall.anm"
                }
            }
            "Spell4_To_Idle" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell_4_cast_to_Idle.anm"
                }
            }
            0xc6b6d6bf = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Old_Morde_Walk.anm"
                }
            }
            "Joke" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "PORO" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 5
                        mEndFrame: f32 = 147
                        mShowSubmeshList: list[hash] = {
                            0x1d850365
                        }
                    }
                    0xeed2417d = SoundEventData {
                        mSoundName: string = "Play_sfx_Mordekaiser_Joke_cast"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Mordekaiser_Joke.anm"
                }
            }
            "Joke_In" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x86509ad3 = SoundEventData {
                        mSoundName: string = "Play_sfx_Mordekaiser_Joke_in_cast"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Mordekaiser_Joke_IdleIn.anm"
                }
            }
            0x38cd12e3 = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = 0x432b1d96
                mEventDataMap: map[hash,pointer] = {
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "mAce"
                        mJointNameToSnapTo: hash = 0xfc1254bb
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell3_Cast_to_Idle.anm"
                }
            }
            "Spell3" = ConditionBoolClipData {
                Updater: pointer = 0x6c816d62 {}
                mChangeAnimationMidPlay: bool = true
                mTrueConditionClipName: hash = 0xde27ecc4
                mFalseConditionClipName: hash = 0x700fcd2f
            }
            "Spell4_To_Run" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell_4_cast_to_run.anm"
                }
            }
            "Dance" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Dance_In"
                    "Dance_Loop"
                }
            }
            "Dance_In" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x125f0a8c = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            0xaf274f0f
                        }
                        mHideSubmeshList: list[hash] = {
                            "mAce"
                        }
                    }
                    0xbc45bbc5 = SoundEventData {
                        mSoundName: string = "Play_sfx_Mordekaiser_Dance_cast"
                        mIsLoop: bool = false
                    }
                    0x4b5da353 = SoundEventData {
                        mSoundName: string = "Play_sfx_Mordekaiser_Dance_loop_crowd"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Dance_Intro.anm"
                }
            }
            "Dance_Loop" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x125f0a8c = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            0xaf274f0f
                        }
                        mHideSubmeshList: list[hash] = {
                            "mAce"
                        }
                    }
                    0xbc45bbc5 = SoundEventData {
                        mStartFrame: f32 = 3
                        mSoundName: string = "Play_sfx_Mordekaiser_Dance_loop"
                    }
                    0x4b5da353 = SoundEventData {
                        mSoundName: string = "Play_sfx_Mordekaiser_Dance_loop_crowd2"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Dance_Loop.anm"
                }
            }
            "Attack1_To_Idle" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/AutoAttack1_to_Idle.anm"
                }
            }
            "Attack2_To_Idle" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/AutoAttack2_to_Idle.anm"
                }
            }
            0x2f52c472 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/AutoAttack1_to_run.anm"
                }
            }
            0x556ce909 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Autoattack2_to_run.anm"
                }
            }
            0x41ef7b02 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Stop" = StopAnimationEventData {
                        mName: hash = "TURN"
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Old_Morde_Walk_to_Battle_Idle.anm"
                }
            }
            0x08935393 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x14afdbac = ParticleEventData {
                        mStartFrame: f32 = 11
                        mEffectKey: hash = "Mordekaiser_W_footstep"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x215c93e3
                            }
                        }
                    }
                    0xc732ff85 = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                    0x4ae08392 = SoundEventData {
                        mStartFrame: f32 = 2
                        mSoundName: string = "Play_sfx_Mordekaiser_walk"
                        mIsKillEvent: bool = false
                    }
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "R_Hand"
                        mJointNameToSnapTo: hash = 0xa09830a0
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell2_Idle_to_Spell2_Walk.anm"
                }
            }
            "Attack_Turret" = AtomicClipData {
                mTrackDataName: hash = 0x432b1d96
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Attack_Turret.anm"
                }
            }
            0x94f4e78c = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "audio_respawn" = SoundEventData {
                        mSoundName: string = "Play_sfx_Mordekaiser_Respawn_cast"
                        mIsLoop: bool = false
                    }
                    "Spawn" = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_Spawn"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsKillEvent: bool = false
                    }
                    "FadeIn" = FadeEventData {
                        mStartFrame: f32 = 0.200000003
                        mTimeToFade: f32 = 1.5
                        mTargetAlpha: f32 = 1
                    }
                    0x86678755 = FadeEventData {
                        mStartFrame: f32 = 0.00100000005
                        mTargetAlpha: f32 = 0
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/respawn_part1.anm"
                }
            }
            0xa0e6dc0c = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Vfx" = ParticleEventData {
                        mStartFrame: f32 = 11
                        mEffectKey: hash = "Mordekaiser_AutoAttack_R2L_A"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                    }
                    0x957977fd = ParticleEventData {
                        mEffectKey: hash = 0x7a9fa5c4
                        mStartFrame: f32 = 11
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                    }
                    0x1e14ea15 = StopAnimationEventData {
                        mEndFrame: f32 = 30
                        mStopAnimationName: hash = 0xf301e808
                    }
                    0x373e9c78 = StopAnimationEventData {
                        mEndFrame: f32 = 30
                        mStopAnimationName: hash = 0x9204de61
                    }
                    0x14f890d7 = StopAnimationEventData {
                        mEndFrame: f32 = 30
                        mStopAnimationName: hash = 0x8dd8b42e
                    }
                    0x7470e324 = StopAnimationEventData {
                        mEndFrame: f32 = 30
                        mStopAnimationName: hash = 0x7470e324
                    }
                    0x5ab4742c = StopAnimationEventData {
                        mEndFrame: f32 = 30
                        mStopAnimationName: hash = 0x46c1234b
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/AutoAttack1.anm"
                }
            }
            "Attack1_Fast" = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Vfx" = ParticleEventData {
                        mStartFrame: f32 = 11
                        mEffectKey: hash = "Mordekaiser_AutoAttack_R2L_A"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                    }
                    0x957977fd = ParticleEventData {
                        mEffectKey: hash = 0x7a9fa5c4
                        mStartFrame: f32 = 11
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/AutoAttack1_Fast.anm"
                }
            }
            "Attack1" = ConditionFloatClipData {
                mConditionFloatPairDataList: list[embed] = {
                    ConditionFloatPairData {
                        mClipName: hash = 0xa0e6dc0c
                    }
                    ConditionFloatPairData {
                        mClipName: hash = "Attack1_Fast"
                        mValue: f32 = 1.39999998
                    }
                }
                Updater: pointer = 0x9c4f3cc3 {}
            }
            0x37cd0512 = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mMaskDataName: hash = 0x432b1d96
                mTrackDataName: hash = 0x432b1d96
                mEventDataMap: map[hash,pointer] = {
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "mAce"
                        mJointNameToSnapTo: hash = 0xfc1254bb
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell3_Cast_Walk_to_Run.anm"
                }
            }
            0xc255baaa = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Battle_Idle_to_Walk.anm"
                }
            }
            0x7ec87e48 = ConditionBoolClipData {
                Updater: pointer = 0x6c816d62 {}
                mChangeAnimationMidPlay: bool = true
                mTrueConditionClipName: hash = 0xc271395a
                mFalseConditionClipName: hash = 0xd680ab49
            }
            0xd680ab49 = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mTrackDataName: hash = 0x432b1d96
                mEventDataMap: map[hash,pointer] = {
                    0x1a606980 = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_E_Cast_Ground"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0xa5db086f = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_E_HandGlow"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xe3da48b0
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "mAce"
                        mJointNameToSnapTo: hash = 0xfc1254bb
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell3_Cast_from_Spell2.anm"
                }
            }
            0xc271395a = AtomicClipData {
                mAnimationInterruptionGroupNames: list[hash] = {
                    "Spells"
                }
                mMaskDataName: hash = 0x432b1d96
                mTrackDataName: hash = 0x432b1d96
                mEventDataMap: map[hash,pointer] = {
                    0xa5db086f = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_E_HandGlow"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xe3da48b0
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x1a606980 = ParticleEventData {
                        mEffectKey: hash = "Mordekaiser_E_Cast_Ground"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0xd9c85bd3 = JointSnapEventData {
                        mIsSelfOnly: bool = true
                        mJointNameToOverride: hash = "mAce"
                        mJointNameToSnapTo: hash = 0xfc1254bb
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell3_Cast_Walk_from_Spell2.anm"
                }
            }
            0x7927a335 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell_4_cast_to_Spell2_Idle.anm"
                }
            }
            0x48067a60 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = 0x0a70dc21
                mEventDataMap: map[hash,pointer] = {
                    "StopTurn" = StopAnimationEventData {
                        mStopAnimationName: hash = "TURN"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell_4_cast_to_Spell2_Run.anm"
                }
            }
            "Recall_Winddown" = SequencerClipData {
                mFlags: u32 = 8
                mClipNameList: list[hash] = {
                    0x94f4e78c
                    0x97f4ec45
                    "Idle_Selector"
                }
            }
            0x135e26c8 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell1_to_Spell2_Idle.anm"
                }
            }
            0x17ad0317 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell1_to_Spell2_run.anm"
                }
            }
            "Channel" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Channel_Wndup"
                    "Channel_Loop"
                }
            }
            0x97f4ec45 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/respawn_part2.anm"
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
            0x432b1d96 = MaskData {
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            0x643a01ca = MaskData {
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            0x7136e1bc = MaskData {
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            0xe6ef5696 = MaskData {
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            0x432b1d96 = TrackData {
                mPriority: u8 = 1
            }
            "Default" = TrackData {
                mPriority: u8 = 2
            }
            "TURN" = TrackData {
                mPriority: u8 = 3
                mBlendMode: u8 = 2
            }
            0xe6ef5696 = TrackData {
                mPriority: u8 = 4
                mBlendMode: u8 = 1
            }
            "Death" = TrackData {}
        }
        mSyncGroupDataMap: map[hash,embed] = {
            0x0a70dc21 = SyncGroupData {
                mType: u32 = 1
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            10234850509117242701 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476870491469 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289110054976845 = TimeBlendData {
                mTime: f32 = 0
            }
            16439539846091423053 = TimeBlendData {
                mTime: f32 = 0
            }
            16367480521181674829 = TimeBlendData {
                mTime: f32 = 0
            }
            16583658495910919501 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634831269197 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556605523311949 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647006022188365 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853230072053069 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339407506765 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413820501325 = TimeBlendData {
                mTime: f32 = 0
            }
            11539948551159479689 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            11539948551109146832 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            11539948551125924451 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            10400565852916481417 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            10400565852866148560 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            10400565852882926179 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            6463208476699408488 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10234850508946159720 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11831733634660186216 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10832289109883893864 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13630352413649418344 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7827523572921153640 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16583658495739836520 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16367480521010591848 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16439539845920340072 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13222943558391445608 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13156647005851105384 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3084207952311498856 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10400565852057778280 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12895556605352228968 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17670928513239496808 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8074898261648226408 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13255853229900970088 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13590883339236423784 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10469693183183173736 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12432335882738350184 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9048391649129281640 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4195074575969957992 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11539948550300776552 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12895556606210932105 = TransitionClipBlendData {
                mClipName: hash = "Spell1_To_Idle"
            }
            12895556606160599248 = TransitionClipBlendData {
                mClipName: hash = "Spell1_To_Idle"
            }
            12895556606177376867 = TransitionClipBlendData {
                mClipName: hash = "Spell1_To_Idle"
            }
            12895556603067846346 = TransitionClipBlendData {
                mClipName: hash = "Spell1_ToRun"
            }
            12895556605036601872 = TransitionClipBlendData {
                mClipName: hash = "Spell1_ToRun"
            }
            12895556603270189393 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556602407870772 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556602963193580 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556605072815694 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556603232185137 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556606474317691 = TimeBlendData {
                mTime: f32 = 0
            }
            3953264719667450193 = TimeBlendData {
                mTime: f32 = 0
            }
            3953264718805131572 = TimeBlendData {
                mTime: f32 = 0
            }
            3953264719360454380 = TimeBlendData {
                mTime: f32 = 0
            }
            3953264721470076494 = TimeBlendData {
                mTime: f32 = 0
            }
            3953264719629445937 = TimeBlendData {
                mTime: f32 = 0
            }
            3953264722871578491 = TimeBlendData {
                mTime: f32 = 0
            }
            249634443740631377 = TimeBlendData {
                mTime: f32 = 0
            }
            249634442878312756 = TimeBlendData {
                mTime: f32 = 0
            }
            249634443433635564 = TimeBlendData {
                mTime: f32 = 0
            }
            249634445543257678 = TimeBlendData {
                mTime: f32 = 0
            }
            249634443702627121 = TimeBlendData {
                mTime: f32 = 0
            }
            249634446944759675 = TimeBlendData {
                mTime: f32 = 0
            }
            2634727742823518545 = TimeBlendData {
                mTime: f32 = 0
            }
            2634727741961199924 = TimeBlendData {
                mTime: f32 = 0
            }
            2634727742516522732 = TimeBlendData {
                mTime: f32 = 0
            }
            2634727744626144846 = TimeBlendData {
                mTime: f32 = 0
            }
            2634727742785514289 = TimeBlendData {
                mTime: f32 = 0
            }
            2634727746027646843 = TimeBlendData {
                mTime: f32 = 0
            }
            11695485729371902289 = TimeBlendData {
                mTime: f32 = 0
            }
            11695485728509583668 = TimeBlendData {
                mTime: f32 = 0
            }
            11695485729064906476 = TimeBlendData {
                mTime: f32 = 0
            }
            11695485731174528590 = TimeBlendData {
                mTime: f32 = 0
            }
            11695485729333898033 = TimeBlendData {
                mTime: f32 = 0
            }
            11695485732576030587 = TimeBlendData {
                mTime: f32 = 0
            }
            3790037683038638417 = TimeBlendData {
                mTime: f32 = 0
            }
            3790037682176319796 = TimeBlendData {
                mTime: f32 = 0
            }
            3790037682731642604 = TimeBlendData {
                mTime: f32 = 0
            }
            3790037684841264718 = TimeBlendData {
                mTime: f32 = 0
            }
            3790037683000634161 = TimeBlendData {
                mTime: f32 = 0
            }
            3790037686242766715 = TimeBlendData {
                mTime: f32 = 0
            }
            17714890971765592401 = TimeBlendData {
                mTime: f32 = 0
            }
            17714890970903273780 = TimeBlendData {
                mTime: f32 = 0
            }
            17714890971458596588 = TimeBlendData {
                mTime: f32 = 0
            }
            17714890973568218702 = TimeBlendData {
                mTime: f32 = 0
            }
            17714890971727588145 = TimeBlendData {
                mTime: f32 = 0
            }
            17714890974969720699 = TimeBlendData {
                mTime: f32 = 0
            }
            7158575871686712140 = TransitionClipBlendData {
                mClipName: hash = "Spell2_Idle_In"
            }
            13222943559250148745 = TransitionClipBlendData {
                mClipName: hash = 0xc0439cdd
            }
            13222943559199815888 = TransitionClipBlendData {
                mClipName: hash = 0xc0439cdd
            }
            13222943559216593507 = TransitionClipBlendData {
                mClipName: hash = 0xc0439cdd
            }
            10400565850877784887 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            1505558569086761064 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13854089354725963880 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            15879233659618080872 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14362433343054035048 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3953264721749489768 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            249634445822670952 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2634727744905558120 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11695485731453941864 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3790037685120677992 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17714890973847631976 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10649963990072309864 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3067419955943585896 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16578443396125177960 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10221117466981316712 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11258661680272783464 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10521779140639996008 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            15677482531575707752 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5847132101403883624 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17510531950253062248 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5098395061192112232 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7158575871038994536 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16008023730071943272 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16951412888616450152 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12895556606046920417 = TransitionClipBlendData {
                mClipName: hash = "Spell1_To_Idle"
            }
            12895556605428454683 = TransitionClipBlendData {
                mClipName: hash = "Spell1_To_Idle"
            }
            11500144137245820301 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11500144138584915337 = TransitionClipBlendData {
                mClipName: hash = "Attack1_To_Idle"
            }
            11500144138534582480 = TransitionClipBlendData {
                mClipName: hash = "Attack1_To_Idle"
            }
            11500144138551360099 = TransitionClipBlendData {
                mClipName: hash = "Attack1_To_Idle"
            }
            11500144138420903649 = TransitionClipBlendData {
                mClipName: hash = "Attack1_To_Idle"
            }
            11500144136603815215 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11500144138450889924 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11500144137410585104 = TransitionClipBlendData {
                mClipName: hash = 0x2f52c472
            }
            12895556602700288394 = TransitionClipBlendData {
                mClipName: hash = "Spell1_To_Idle"
            }
            13255853227249029514 = TransitionClipBlendData {
                mClipName: hash = "Spell4_To_Idle"
            }
            13255853230595661537 = TransitionClipBlendData {
                mClipName: hash = "Spell4_To_Idle"
            }
            13255853229977195803 = TransitionClipBlendData {
                mClipName: hash = "Spell4_To_Idle"
            }
            13255853230759673225 = TransitionClipBlendData {
                mClipName: hash = "Spell4_To_Idle"
            }
            13255853230709340368 = TransitionClipBlendData {
                mClipName: hash = "Spell4_To_Idle"
            }
            13255853230726117987 = TransitionClipBlendData {
                mClipName: hash = "Spell4_To_Idle"
            }
            15879233657333698250 = TransitionClipBlendData {
                mClipName: hash = 0xc6b6d6bf
            }
            16583658493455453898 = TransitionClipBlendData {
                mClipName: hash = 0xc6b6d6bf
            }
            16367480518726209226 = TransitionClipBlendData {
                mClipName: hash = 0xc6b6d6bf
            }
            16439539843635957450 = TransitionClipBlendData {
                mClipName: hash = 0xc6b6d6bf
            }
            3084207953170201993 = TransitionClipBlendData {
                mClipName: hash = 0xc6b6d6bf
            }
            3084207953119869136 = TransitionClipBlendData {
                mClipName: hash = 0xc6b6d6bf
            }
            3084207953136646755 = TransitionClipBlendData {
                mClipName: hash = 0xc6b6d6bf
            }
            16583658495424209424 = TransitionClipBlendData {
                mClipName: hash = 0xc6b6d6bf
            }
            16367480520694964752 = TransitionClipBlendData {
                mClipName: hash = 0xc6b6d6bf
            }
            16439539845604712976 = TransitionClipBlendData {
                mClipName: hash = 0xc6b6d6bf
            }
            13854089354410336784 = TransitionClipBlendData {
                mClipName: hash = 0xc6b6d6bf
            }
            13987674971168453702 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13222943558645724230 = TransitionClipBlendData {
                mClipName: hash = "Joke_In"
            }
            1505558569341039686 = TransitionClipBlendData {
                mClipName: hash = "Joke_In"
            }
            11539948550555055174 = TransitionClipBlendData {
                mClipName: hash = "Joke_In"
            }
            6463208475577011503 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1505558567964364079 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13854089353603566895 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10234850507823762735 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11831733633537789231 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10832289108761496879 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13630352412527021359 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7827523571798756655 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13222943557269048623 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16583658494617439535 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16367480519888194863 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16439539844797943087 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            15879233658495683887 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14318868182978252079 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13987674969791778095 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16525775250434018607 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13156647004728708399 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12059822171054132527 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11453659671199468847 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3084207951189101871 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10400565850935381295 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12895556604229831983 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14362433341931638063 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3953264720627092783 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            249634444700273967 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2634727743783161135 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11695485730331544879 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3790037683998281007 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17714890972725234991 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10649963988949912879 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3067419954821188911 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16578443395002780975 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10221117465858919727 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11258661679150386479 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10521779139517599023 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            15677482530453310767 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5847132100281486639 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17510531949130665263 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5098395060069715247 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7158575869916597551 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17670928512117099823 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675254049328431 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8074898260525829423 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4092948404396608815 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13255853228778573103 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16951412887494053167 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13590883338114026799 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10469693182060776751 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12432335881615953199 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9048391648006884655 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4195074574847561007 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11539948549178379567 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11539948547648835978 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            10400565849405837706 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            14318868181448708490 = TransitionClipBlendData {
                mClipName: hash = 0x41ef7b02
            }
            13255853229585342992 = TransitionClipBlendData {
                mClipName: hash = "Spell4_To_Run"
            }
            13255853227616587466 = TransitionClipBlendData {
                mClipName: hash = "Spell4_To_Run"
            }
            8351779190699598352 = TransitionClipBlendData {
                mClipName: hash = "Spell4_To_Run"
            }
            3953264721433862672 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3084207950813851101 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10400565850560130525 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6463208477558111625 = TransitionClipBlendData {
                mClipName: hash = "Attack2_To_Idle"
            }
            6463208477507778768 = TransitionClipBlendData {
                mClipName: hash = "Attack2_To_Idle"
            }
            6463208477524556387 = TransitionClipBlendData {
                mClipName: hash = "Attack2_To_Idle"
            }
            6463208477394099937 = TransitionClipBlendData {
                mClipName: hash = "Attack2_To_Idle"
            }
            6463208474415025866 = TransitionClipBlendData {
                mClipName: hash = 0x556ce909
            }
            6463208476383781392 = TransitionClipBlendData {
                mClipName: hash = 0x556ce909
            }
            3410003862496300746 = TimeBlendData {
                mTime: f32 = 0
            }
            3410003864465056272 = TimeBlendData {
                mTime: f32 = 0
            }
            6155551018259456528 = TimeBlendData {
                mTime: f32 = 0
            }
            6155551017994173321 = TimeBlendData {
                mTime: f32 = 0
            }
            6155551016290701002 = TimeBlendData {
                mTime: f32 = 0
            }
            11480947152047132362 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8290604741173268170 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8290604744316353929 = TimeBlendData {
                mTime: f32 = 0
            }
            8290604744266021072 = TimeBlendData {
                mTime: f32 = 0
            }
            8290604744282798691 = TimeBlendData {
                mTime: f32 = 0
            }
            8290604744152342241 = TimeBlendData {
                mTime: f32 = 0
            }
            11480947155190218121 = TimeBlendData {
                mTime: f32 = 0
            }
            11480947155139885264 = TimeBlendData {
                mTime: f32 = 0
            }
            11480947155156662883 = TimeBlendData {
                mTime: f32 = 0
            }
            11480947155026206433 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208474047467914 = TransitionClipBlendData {
                mClipName: hash = "Attack2_To_Idle"
            }
            11480947151679574410 = TimeBlendData {
                mTime: f32 = 0
            }
            8290604740805710218 = TimeBlendData {
                mTime: f32 = 0
            }
            3410003862128742794 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            6155551015923143050 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            15677482530239962835 = TransitionClipBlendData {
                mClipName: hash = 0x08935393
            }
            17510531948917317331 = TransitionClipBlendData {
                mClipName: hash = 0x08935393
            }
            17510531947394454419 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            12895556605693762823 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11480947153851123085 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3410003864300291469 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            6463208476219016589 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8290604742977258893 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            6155551018094691725 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            1505558568606369165 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13854089354245571981 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10234850508465767821 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11831733634179794317 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10832289109403501965 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061686588813 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            2291038461329933709 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13630352413169026445 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            7827523572440761741 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13222943557911053709 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16583658495259444621 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16367480520530199949 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16439539845439948173 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            15879233659137688973 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            14318868183620257165 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13987674970433783181 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16525775251076023693 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13156647005370713485 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            4751151382941402509 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            12059822171696137613 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11453659671841473933 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3084207951831106957 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10400565851577386381 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            14362433342573643149 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3953264721269097869 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            249634445342279053 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            2634727744425166221 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11695485730973549965 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3790037684640286093 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            17714890973367240077 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10649963989591917965 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3067419955463193997 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16578443395644786061 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10221117466500924813 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11258661679792391565 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10521779140159604109 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            15677482531095315853 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            5847132100923491725 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            617929467227276685 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8390455852071650701 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            17510531949772670349 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            5098395060711720333 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            7158575870558602637 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            17670928512759104909 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13039675254691333517 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8074898261167834509 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            4092948405038613901 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16008023729591551373 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13255853229420578189 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16951412888136058253 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8351779190534833549 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13793459113404138893 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13590883338756031885 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10469693182702781837 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            12432335882257958285 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            9048391648648889741 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            4195074575489566093 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11539948549820384653 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11480947155553282048 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3410003866002450432 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            6463208477921175552 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8290604744679417856 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            6155551019796850688 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            18143006189783934976 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            1505558570308528128 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13854089355947730944 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10234850510167926784 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11831733635881953280 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10832289111105660928 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854063388747776 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            2291038463032092672 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13630352414871185408 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            7827523574142920704 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13222943559613212672 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16583658496961603584 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16367480522232358912 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16439539847142107136 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            15879233660839847936 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            14318868185322416128 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13987674972135942144 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16525775252778182656 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13156647007072872448 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            4751151384643561472 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            12059822173398296576 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11453659673543632896 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3084207953533265920 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10400565853279545344 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            12895556606573996032 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11500144138947979264 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            14362433344275802112 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3953264722971256832 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            249634447044438016 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            2634727746127325184 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11695485732675708928 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3790037686342445056 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            17714890975069399040 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10649963991294076928 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3067419957165352960 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16578443397346945024 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10221117468203083776 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11258661681494550528 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10521779141861763072 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            15677482532797474816 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            5847132102625650688 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            617929468929435648 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8390455853773809664 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            17510531951474829312 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            5098395062413879296 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            7158575872260761600 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            17670928514461263872 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13039675256393492480 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8074898262869993472 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            4092948406740772864 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16008023731293710336 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13255853231122737152 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16951412889838217216 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8351779192236992512 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13793459115106297856 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13590883340458190848 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10469693184404940800 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            12432335883960117248 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            9048391650351048704 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            4195074577191725056 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11539948551522543616 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11453659671818463116 = TimeBlendData {
                mTime: f32 = 0
            }
            8074898258996285834 = TransitionClipBlendData {
                mClipName: hash = 0x38cd12e3
            }
            16008023728891949879 = TransitionClipBlendData {
                mClipName: hash = 0x37cd0512
            }
            16008023729756316176 = TransitionClipBlendData {
                mClipName: hash = 0x37cd0512
            }
            14362433342738407952 = TransitionClipBlendData {
                mClipName: hash = "Spell1_ToRun"
            }
            8074898261724452123 = TransitionClipBlendData {
                mClipName: hash = 0xc0439cdd
            }
            8074898262506929545 = TransitionClipBlendData {
                mClipName: hash = 0xc0439cdd
            }
            8074898262456596688 = TransitionClipBlendData {
                mClipName: hash = 0xc0439cdd
            }
            8074898262473374307 = TransitionClipBlendData {
                mClipName: hash = 0xc0439cdd
            }
            6247030500847766831 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2005863781968629039 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11594196236689722671 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11480947153209117999 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3410003863658286383 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8290604742335253807 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6155551017452686639 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            18143006187439770927 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16852854061044583727 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            2291038460687928623 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4751151382299397423 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            617929466585271599 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8390455851429645615 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16008023728949546287 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4020875619059354927 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8351779189892828463 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13793459112762133807 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6247030502694841540 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2005863783815703748 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11594196238536797380 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11480947155056192708 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3410003865505361092 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6463208477424086212 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8290604744182328516 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6155551019299761348 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            18143006189286845636 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1505558569811438788 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13854089355450641604 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10234850509670837444 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11831733635384863940 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10832289110608571588 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16852854062891658436 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            2291038462535003332 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13630352414374096068 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7827523573645831364 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13222943559116123332 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16583658496464514244 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16367480521735269572 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16439539846645017796 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            15879233660342758596 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14318868184825326788 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13987674971638852804 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16525775252281093316 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13156647006575783108 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4751151384146472132 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12059822172901207236 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11453659673046543556 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3084207953036176580 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10400565852782456004 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12895556606076906692 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14362433343778712772 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3953264722474167492 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            249634446547348676 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2634727745630235844 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11695485732178619588 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3790037685845355716 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17714890974572309700 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10649963990796987588 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3067419956668263620 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16578443396849855684 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10221117467705994436 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11258661680997461188 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10521779141364673732 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            15677482532300385476 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5847132102128561348 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            617929468432346308 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8390455853276720324 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17510531950977739972 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5098395061916789956 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7158575871763672260 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17670928513964174532 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675255896403140 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4092948406243683524 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16008023730796620996 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4020875620906429636 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13255853230625647812 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16951412889341127876 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8351779191739903172 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13793459114609208516 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13590883339961101508 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10469693183907851460 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12432335883463027908 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9048391649853959364 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4195074576694635716 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11539948551025454276 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6247030501654536720 = TransitionClipBlendData {
                mClipName: hash = 0x2f52c472
            }
            6247030499685781194 = TransitionClipBlendData {
                mClipName: hash = 0x2f52c472
            }
            6247030502828866953 = TransitionClipBlendData {
                mClipName: hash = "Attack1_To_Idle"
            }
            6247030502778534096 = TransitionClipBlendData {
                mClipName: hash = "Attack1_To_Idle"
            }
            6247030502795311715 = TransitionClipBlendData {
                mClipName: hash = "Attack1_To_Idle"
            }
            6247030502664855265 = TransitionClipBlendData {
                mClipName: hash = "Attack1_To_Idle"
            }
            6247030499318223242 = TransitionClipBlendData {
                mClipName: hash = "Attack1_To_Idle"
            }
            2005863780439085450 = TransitionClipBlendData {
                mClipName: hash = "Attack1_To_Idle"
            }
            11594196235160179082 = TransitionClipBlendData {
                mClipName: hash = "Attack1_To_Idle"
            }
            2005863782775398928 = TransitionClipBlendData {
                mClipName: hash = 0x2f52c472
            }
            11594196237496492560 = TransitionClipBlendData {
                mClipName: hash = 0x2f52c472
            }
            1505558568771133968 = TransitionClipBlendData {
                mClipName: hash = 0xc255baaa
            }
            13222943558075818512 = TransitionClipBlendData {
                mClipName: hash = 0xc255baaa
            }
            14003303856036172170 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            11539948549985149456 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6247030502228081322 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2005863783348943530 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11594196238070037162 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11480947154589432490 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3410003865038600874 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6463208476957325994 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8290604743715568298 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6155551018833001130 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            18143006188820085418 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1505558569344678570 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13854089354983881386 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14003303858946030250 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10234850509204077226 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11831733634918103722 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10832289110141811370 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16852854062424898218 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            2291038462068243114 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13630352413907335850 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7827523573179071146 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13222943558649363114 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16583658495997754026 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16367480521268509354 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16439539846178257578 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            15879233659875998378 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14318868184358566570 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13987674971172092586 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16525775251814333098 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13156647006109022890 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4751151383679711914 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12059822172434447018 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11453659672579783338 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3084207952569416362 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10400565852315695786 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12895556605610146474 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11500144137984129706 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14362433343311952554 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3953264722007407274 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            249634446080588458 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2634727745163475626 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11695485731711859370 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3790037685378595498 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17714890974105549482 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10649963990330227370 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3067419956201503402 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16578443396383095466 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10221117467239234218 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11258661680530700970 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10521779140897913514 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            15677482531833625258 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5847132101661801130 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            617929467965586090 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8390455852809960106 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17510531950510979754 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5098395061450029738 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7158575871296912042 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17670928513497414314 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675255429642922 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8074898261906143914 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4092948405776923306 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16008023730329860778 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4020875620439669418 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13255853230158887594 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16951412888874367658 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8351779191273142954 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13793459114142448298 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13590883339494341290 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10469693183441091242 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12432335882996267690 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9048391649387199146 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4195074576227875498 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11539948550558694058 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13255853230548687692 = TransitionClipBlendData {
                mClipName: hash = 0x7927a335
            }
            13255853228565225171 = TransitionClipBlendData {
                mClipName: hash = 0x48067a60
            }
            8730125852376325843 = TransitionClipBlendData {
                mClipName: hash = 0x48067a60
            }
            12895556604771318665 = TransitionClipBlendData {
                mClipName: hash = "Spell1_ToRun"
            }
            13156647005347702668 = TimeBlendData {
                mTime: f32 = 0
            }
            4751151382918391692 = TimeBlendData {
                mTime: f32 = 0
            }
            12059822171673126796 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207951808096140 = TimeBlendData {
                mTime: f32 = 0
            }
            10400565851554375564 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556604848826252 = TimeBlendData {
                mTime: f32 = 0
            }
            11500144137222809484 = TimeBlendData {
                mTime: f32 = 0
            }
            14362433342550632332 = TimeBlendData {
                mTime: f32 = 0
            }
            3953264721246087052 = TimeBlendData {
                mTime: f32 = 0
            }
            249634445319268236 = TimeBlendData {
                mTime: f32 = 0
            }
            2634727744402155404 = TimeBlendData {
                mTime: f32 = 0
            }
            11695485730950539148 = TimeBlendData {
                mTime: f32 = 0
            }
            3790037684617275276 = TimeBlendData {
                mTime: f32 = 0
            }
            17714890973344229260 = TimeBlendData {
                mTime: f32 = 0
            }
            10649963989568907148 = TimeBlendData {
                mTime: f32 = 0
            }
            3067419955440183180 = TimeBlendData {
                mTime: f32 = 0
            }
            16578443395621775244 = TimeBlendData {
                mTime: f32 = 0
            }
            10221117466477913996 = TimeBlendData {
                mTime: f32 = 0
            }
            11258661679769380748 = TimeBlendData {
                mTime: f32 = 0
            }
            10521779140136593292 = TimeBlendData {
                mTime: f32 = 0
            }
            15677482531072305036 = TimeBlendData {
                mTime: f32 = 0
            }
            5847132100900480908 = TimeBlendData {
                mTime: f32 = 0
            }
            617929467204265868 = TimeBlendData {
                mTime: f32 = 0
            }
            8390455852048639884 = TimeBlendData {
                mTime: f32 = 0
            }
            17510531949749659532 = TimeBlendData {
                mTime: f32 = 0
            }
            5098395060688709516 = TimeBlendData {
                mTime: f32 = 0
            }
            7158575870535591820 = TimeBlendData {
                mTime: f32 = 0
            }
            17670928512736094092 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675254668322700 = TimeBlendData {
                mTime: f32 = 0
            }
            8074898261144823692 = TimeBlendData {
                mTime: f32 = 0
            }
            15456542253655582604 = TimeBlendData {
                mTime: f32 = 0
            }
            4092948405015603084 = TimeBlendData {
                mTime: f32 = 0
            }
            16008023729568540556 = TimeBlendData {
                mTime: f32 = 0
            }
            14011042976935241612 = TimeBlendData {
                mTime: f32 = 0
            }
            4020875619678349196 = TimeBlendData {
                mTime: f32 = 0
            }
            9135690694322874252 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853229397567372 = TimeBlendData {
                mTime: f32 = 0
            }
            16951412888113047436 = TimeBlendData {
                mTime: f32 = 0
            }
            8351779190511822732 = TimeBlendData {
                mTime: f32 = 0
            }
            13793459113381128076 = TimeBlendData {
                mTime: f32 = 0
            }
            8730125853208668044 = TimeBlendData {
                mTime: f32 = 0
            }
            5189970175825602444 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883338733021068 = TimeBlendData {
                mTime: f32 = 0
            }
            10469693182679771020 = TimeBlendData {
                mTime: f32 = 0
            }
            12432335882234947468 = TimeBlendData {
                mTime: f32 = 0
            }
            9048391648625878924 = TimeBlendData {
                mTime: f32 = 0
            }
            4195074575466555276 = TimeBlendData {
                mTime: f32 = 0
            }
            11539948549797373836 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030501466761100 = TimeBlendData {
                mTime: f32 = 0
            }
            2005863782587623308 = TimeBlendData {
                mTime: f32 = 0
            }
            11594196237308716940 = TimeBlendData {
                mTime: f32 = 0
            }
            11480947153828112268 = TimeBlendData {
                mTime: f32 = 0
            }
            3410003864277280652 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476196005772 = TimeBlendData {
                mTime: f32 = 0
            }
            8290604742954248076 = TimeBlendData {
                mTime: f32 = 0
            }
            6155551018071680908 = TimeBlendData {
                mTime: f32 = 0
            }
            18143006188058765196 = TimeBlendData {
                mTime: f32 = 0
            }
            1505558568583358348 = TimeBlendData {
                mTime: f32 = 0
            }
            13854089354222561164 = TimeBlendData {
                mTime: f32 = 0
            }
            14003303858184710028 = TimeBlendData {
                mTime: f32 = 0
            }
            10234850508442757004 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634156783500 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289109380491148 = TimeBlendData {
                mTime: f32 = 0
            }
            16852854061663577996 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            2291038461306922892 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413146015628 = TimeBlendData {
                mTime: f32 = 0
            }
            7827523572417750924 = TimeBlendData {
                mTime: f32 = 0
            }
            13222943557888042892 = TimeBlendData {
                mTime: f32 = 0
            }
            16583658495236433804 = TimeBlendData {
                mTime: f32 = 0
            }
            16367480520507189132 = TimeBlendData {
                mTime: f32 = 0
            }
            16439539845416937356 = TimeBlendData {
                mTime: f32 = 0
            }
            15879233659114678156 = TimeBlendData {
                mTime: f32 = 0
            }
            14318868183597246348 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674970410772364 = TimeBlendData {
                mTime: f32 = 0
            }
            16525775251053012876 = TimeBlendData {
                mTime: f32 = 0
            }
            10733458403099025936 = TransitionClipBlendData {
                mClipName: hash = 0xc6b6d6bf
            }
            1505558569945464201 = TransitionClipBlendData {
                mClipName: hash = 0xc0439cdd
            }
            1505558569895131344 = TransitionClipBlendData {
                mClipName: hash = 0xc0439cdd
            }
            1505558569911908963 = TransitionClipBlendData {
                mClipName: hash = 0xc0439cdd
            }
            12895556604016484051 = TransitionClipBlendData {
                mClipName: hash = 0x17ad0317
            }
            12895556605999946572 = TransitionClipBlendData {
                mClipName: hash = 0x135e26c8
            }
            13222943555739505034 = TimeBlendData {
                mTime: f32 = 0.400000006
            }
            3953264719097549194 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            249634443170730378 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            2634727742253617546 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            11695485728802001290 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            3790037682468737418 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            17714890971195691402 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            13590883336584483210 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            11539948550377002267 = TimeBlendData {
                mTime: f32 = 0.150000006
            }
            14003303858764338459 = TimeBlendData {
                mTime: f32 = 0.150000006
            }
            8351779188363284874 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            16583658496598539657 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            16583658496548206800 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            16583658496564984419 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            16367480521869294985 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            16367480521818962128 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            16367480521835739747 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            16439539846779043209 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            16439539846728710352 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            16439539846745487971 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            6247030502891543930 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            2005863784012406138 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11594196238733499770 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11480947155252895098 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3410003865702063482 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            6463208477620788602 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8290604744379030906 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            6155551019496463738 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            18143006189483548026 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            1505558570008141178 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13854089355647343994 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            14003303859609492858 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10234850509867539834 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11831733635581566330 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10832289110805273978 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854063088360826 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            2291038462731705722 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13630352414570798458 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            7827523573842533754 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13222943559312825722 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16583658496661216634 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16367480521931971962 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16439539846841720186 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            15879233660539460986 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            14318868185022029178 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13987674971835555194 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16525775252477795706 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13156647006772485498 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            4751151384343174522 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            12059822173097909626 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11453659673243245946 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10733458404336033146 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3084207953232878970 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10400565852979158394 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            12895556606273609082 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11500144138647592314 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            14362433343975415162 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            1395595578890607994 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            1706023235086278010 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3953264722670869882 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            249634446744051066 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            2634727745826938234 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11695485732375321978 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3790037686042058106 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            17714890974769012090 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10649963990993689978 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            3067419956864966010 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16578443397046558074 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10221117467902696826 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11258661681194163578 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10521779141561376122 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            15677482532497087866 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            5847132102325263738 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            617929468629048698 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8390455853473422714 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            17510531951174442362 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            5098395062113492346 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            7158575871960374650 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            17670928514160876922 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13039675256093105530 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8074898262569606522 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            15456542255080365434 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            4092948406440385914 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16008023730993323386 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            14011042978360024442 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            4020875621103132026 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            9135690695747657082 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13255853230822350202 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16951412889537830266 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8351779191936605562 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13793459114805910906 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            8730125854633450874 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            5189970177250385274 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            13590883340157803898 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            10469693184104553850 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            12432335883659730298 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            9048391650050661754 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            4195074576891338106 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            11539948551222156666 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854059164499968 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060619000100 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854059631526523 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061863984140 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061837616283 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854059958453362 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060669332957 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061094806806 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060597700873 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854059515040138 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062390156509 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061547486799 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061919290125 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854059697923927 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062338063693 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060986987319 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062243206427 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854063025683849 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062975350992 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062992128611 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062861672161 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062498371263 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062421259334 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854063012206856 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062227770558 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060270713602 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061972396126 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061831262921 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854059882598090 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061586070409 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062166980712 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061842085929 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062508514567 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854059489437384 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854059561714455 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060084941137 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854059222622516 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854059777945324 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061887567438 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060046936881 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854063289069435 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061644137938 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854059878689330 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854063024469614 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061544289326 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061785861413 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061614292577 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062814698316 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060525891498 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854059308372883 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061118055204 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854063241488392 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060351562571 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060831235795 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854063278833627 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062200535950 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062763256649 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060117463779 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060100683026 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061291568712 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062250868807 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854063111308341 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061109050092 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062376039931 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061197140789 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060372884064 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062328874083 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061602165370 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062059128733 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061271242819 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854060141241881 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854061851353616 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
            16852854062426700122 = TimeBlendData {
                mTime: f32 = 0.0500000007
            }
        }
    }
}
