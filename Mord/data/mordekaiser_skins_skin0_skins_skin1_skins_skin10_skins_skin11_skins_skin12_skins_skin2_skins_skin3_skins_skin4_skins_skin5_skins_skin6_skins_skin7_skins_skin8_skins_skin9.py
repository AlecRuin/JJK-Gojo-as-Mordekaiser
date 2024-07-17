#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Spawn" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.25
                }
                ParticleLinger: option[f32] = {
                    1.5
                }
                Lifetime: option[f32] = {
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "dissolveDark"
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 1, 0 }
                }
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 10 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.00416666688
                            0.127048612
                            0.224079862
                            0.287499994
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x4dbd1600: embed = ValueVector3 {
                        ConstantValue: vec3 = { 0, 1, 0 }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.0341887958
                            0.262995899
                            0.686770856
                            0.861436427
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0, 0, 1 }
                            { 0, 0, 0.0575851388, 0.543859661 }
                            { 0, 0.152941182, 0.13333334, 1 }
                            { 0, 0.184313729, 0.184313729, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 2
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.276527077
                                0.70874089
                                0.800000012
                            }
                            Values: list[f32] = {
                                0.00432900432
                                0.353417277
                                0.755705357
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.300000012
                    ErosionFeatherOut: f32 = 0.300000012
                    ErosionSliceWidth: f32 = 1.20000005
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_R_Ground_A_Errode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                DepthBiasFactors: vec2 = { -1, -10 }
                DisableBackfaceCull: bool = true
                ParticleIsLocalOrientation: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.0129032256
                            0.35190919
                            0.994000018
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.5, 1.25, 1.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_CausticShade_Add.dds"
                UvMode: u8 = 1
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { -0.100000001, -0.25 }
                }
                EmitterUvScrollRate: vec2 = { 0, -1 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLinger: option[f32] = {
                    2
                }
                Lifetime: option[f32] = {
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "CoreUnderDark"
                Disabled: bool = true
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 200, 0 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 2, 0 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 50, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 2
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.858823538, 0.862745106, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0145161292
                            0.540045738
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.858823538, 0.862745106, 0 }
                            { 1, 0.858823538, 0.862745106, 1 }
                            { 1, 0.858823538, 0.862745106, 1 }
                            { 1, 0.858823538, 0.862745106, 0 }
                        }
                    }
                }
                Pass: i16 = -1
                DisableBackfaceCull: bool = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 120, 120, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.5, 0.5, 5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_W_bigglow02.dds"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 30
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.132258058
                                    0.214516133
                                    0.338709682
                                    0.554838717
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    0.0917197466
                                    0.254777074
                                    0.647133768
                                    0.904458582
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1.5
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    3
                }
                Lifetime: option[f32] = {
                    1
                }
                FieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    FieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            Radius: embed = ValueFloat {
                                ConstantValue: f32 = 900
                            }
                            Frequency: embed = ValueFloat {
                                ConstantValue: f32 = 800
                            }
                            VelocityDelta: embed = ValueFloat {
                                ConstantValue: f32 = 5
                            }
                            AxisFraction: vec3 = { 1, 0, 1 }
                        }
                    }
                }
                EmitterName: string = "EMBERS"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 100, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 100, 100, 0 }
                        }
                    }
                }
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -400 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, -400 }
                            { 0, 0, -0 }
                        }
                    }
                }
                Drag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.5, 0.5, 0.5 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.5, 0.5, 0.5 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Flags: u8 = 1
                    Radius: f32 = 80
                    Height: f32 = 80
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 20, -40 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 20, -40 }
                        }
                    }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Veigar/Skins/Base/Particles/common_color-smoke32_07.dds"
                BlendMode: u8 = 2
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.945098042, 0.592156887, 0.545098066, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            -0.00498338882
                            0.237541527
                            0.991694331
                        }
                        Values: list[vec4] = {
                            { 0.945098042, 0.592156887, 0.545098066, 0 }
                            { 0.945098042, 0.592156887, 0.545098066, 1 }
                            { 0.945098042, 0.592156887, 0.545098066, 1 }
                        }
                    }
                }
                Pass: i16 = 10
                MeshRenderFlags: u8 = 0
                ColorRenderFlags: u8 = 1
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 8, 8, 8 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0.00281293946
                            0.100923277
                            0.263368279
                            1
                        }
                        Values: list[vec3] = {
                            { 8, 8, 8 }
                            { 2.70063686, 2.78195262, 2.78195262 }
                            { 1.12101912, 1.05689144, 1.10784686 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 9, 9, 9 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 9, 9, 9 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0755007714
                            0.869799674
                            1
                        }
                        Values: list[vec3] = {
                            { 0.75, 0.75, 0.75 }
                            { 1.70000005, 1.70000005, 1.70000005 }
                            { 1.70000005, 1.70000005, 1.70000005 }
                            { 0.150000006, 0.150000006, 0.150000006 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Embers.dds"
                NumFrames: u16 = 3
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                ParticleLinger: option[f32] = {
                    2
                }
                Lifetime: option[f32] = {
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "UnderGlow"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 500, 0 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 2, 0 }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 30, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 1, 0.970000744, 0.510002315 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0145161292
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 1, 0.970000744, 0 }
                            { 0, 1, 0.970000744, 0.510002315 }
                            { 0, 1, 0.970000744, 0 }
                        }
                    }
                }
                Pass: i16 = 99
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsRotationEnabled: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 250, 300, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 0.5, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_R_spotLight.dds"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 90
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.800000012
                                    1.29999995
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            90
                        }
                    }
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.5
                }
                ParticleLinger: option[f32] = {
                    11
                }
                Lifetime: option[f32] = {
                    0.800000012
                }
                EmitterLinger: option[f32] = {
                    1.5
                }
                EmitterName: string = "darkMistBurst"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 300, 800, -700 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 300, 800, -700 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 6, 4 }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 0.600000024
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Flags: u8 = 1
                    Radius: f32 = 2
                    Height: f32 = 80
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 30, 80 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 30, 80 }
                        }
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.223529413, 0.223529413, 0.223529413, 0.78039217 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00896057393
                            0.0601670891
                            0.172929764
                            0.275979221
                            0.620023131
                            0.996415794
                        }
                        Values: list[vec4] = {
                            { 0.223529413, 0.223529413, 0.223529413, 0.00612072274 }
                            { 0.223529413, 0.223529413, 0.223529413, 0.78039217 }
                            { 0.223529413, 0.223529413, 0.223529413, 0.78039217 }
                            { 0.223529413, 0.223529413, 0.223529413, 0.435868651 }
                            { 0.223529413, 0.223529413, 0.223529413, 0.108775891 }
                            { 0.223529413, 0.223529413, 0.223529413, 0 }
                        }
                    }
                }
                Pass: i16 = 6
                AlphaRef: u8 = 0
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.320493072
                                0.634822786
                                1
                            }
                            Values: list[f32] = {
                                0
                                0.261146486
                                0.853503168
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.5
                    ErosionFeatherOut: f32 = 0.5
                    ErosionSliceWidth: f32 = 1
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_Wispy.dds"
                }
                DisableBackfaceCull: bool = true
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    350
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { -100, 0, 0 }
                            { 100, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 15, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.378571421
                                    0.521428585
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.100000001
                                    0.249044582
                                    0.87961781
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 200, 15, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.00457665883
                            0.259581864
                            0.58839184
                            0.925672233
                            1
                        }
                        Values: list[vec3] = {
                            { 0.252688169, 1, 1 }
                            { 0.414864004, 1, 1 }
                            { 0.606135368, 1, 1 }
                            { 0.935520887, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_Wispy.dds"
                NumFrames: u16 = 4
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
                TexDiv: vec2 = { 2, 2 }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_E_Fire_Mult.dds"
                    TexDivMult: vec2 = { 2, 2 }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, -1.25 }
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 1 }
                        Dynamics: pointer = VfxAnimatedVector2fVariableData {
                            ProbabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    KeyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    KeyValues: list[f32] = {
                                        1
                                        -1
                                    }
                                }
                                VfxProbabilityTableData {
                                    KeyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    KeyValues: list[f32] = {
                                        1
                                        -1
                                    }
                                }
                            }
                            Times: list[f32] = {
                                0
                            }
                            Values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.100000001
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 30
                }
                ParticleLifetime: embed = ValueFloat {
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            3
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    11
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "startBlast"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 800, 0, 800 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    12
                                }
                                KeyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 800, 0, 800 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 0, 5 }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, 15, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 15, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 0.300000012
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Radius: f32 = 30
                    Height: f32 = 5
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 50, 0 }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.0117647061, 0.254901975, 0.262745112, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.0117647061, 0.254901975, 0.262745112, 1 }
                            { 0.0117647061, 0.254901975, 0.262745112, 1 }
                            { 0.0105883246, 0.229413703, 0.236472592, 0.669993162 }
                            { 0.0117647061, 0.254901975, 0.262745112, 0 }
                        }
                    }
                }
                Pass: i16 = 7
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.150000006
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherOut: f32 = 0.200000003
                    ErosionSliceWidth: f32 = 1.70000005
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_W_SmokeErode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 90, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 90, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 30, 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 30, 1, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 1, 1 }
                            { 1, 2, 2 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Sion_Skin05_Sl_Dust_01.dds"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 50
                }
                ParticleLifetime: embed = ValueFloat {
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            3
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    11
                }
                Lifetime: option[f32] = {
                    1
                }
                EmitterName: string = "startDirt"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 600, 0, 600 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    12
                                }
                                KeyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 600, 0, 600 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 0, 5 }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, 15, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 15, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 0.200000003
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Radius: f32 = 1
                    Height: f32 = 5
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 50, 0 }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.0549019612, 0.384313732, 0.372549027, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0732265413
                            0.200000003
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.0549019612, 0.384313732, 0.372549027, 0 }
                            { 0.0549019612, 0.384313732, 0.372549027, 1 }
                            { 0.0549019612, 0.384313732, 0.372549027, 1 }
                            { 0.0494121835, 0.345885277, 0.335296959, 0.669993162 }
                            { 0.0549019612, 0.384313732, 0.372549027, 0 }
                        }
                    }
                }
                Pass: i16 = 8
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.150000006
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherOut: f32 = 0.200000003
                    ErosionSliceWidth: f32 = 1.70000005
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_W_SmokeErode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 90, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 90, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 50, 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 50, 1, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 1, 1 }
                            { 1, 2, 2 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Sion_Skin05_Sl_Dust_01.dds"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.150000006
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 120
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2.5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.503432512
                                    0.82837528
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.300000012
                                    0.427956998
                                    0.66989249
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            2.5
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    3
                }
                Lifetime: option[f32] = {
                    0.600000024
                }
                EmitterName: string = "tendrils"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { -100, 0, 0 }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Radius: f32 = 150
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_Cast_Tendrils.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 0.215686277, 0.250980407, 1 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0696969703
                            0.836559117
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 3
                AlphaRef: u8 = 0
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 120
                }
                DisableBackfaceCull: bool = true
                IsRandomStartFrame: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -70, 0, 45 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { -70, 0, 45 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.5, 2, 1.5 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.571428597
                                    0.857142866
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.200000003
                                    0.354838699
                                    0.561290324
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1.5, 2, 1.5 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.151612908
                            0.304285079
                            0.472580642
                            0.770967722
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1.59574473 }
                            { 1, 1, 3 }
                            { 1, 1, 2.73049641 }
                            { 1, 1, 1.48226953 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_Tendrils.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { -1, 0 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_Tendrils_Mult.dds"
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.5
                }
                ParticleLinger: option[f32] = {
                    2
                }
                Lifetime: option[f32] = {
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "FlatUnderDark"
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 2, 0 }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Flags: u8 = 1
                    Radius: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 2
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.340001523, 0.409994662, 0.680003047 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0145161292
                            0.778032064
                            0.821510315
                            0.954233408
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.340001523, 0.409994662, 0 }
                            { 1, 0.340001523, 0.409994662, 0.680003047 }
                            { 1, 0.340001523, 0.409994662, 0.680003047 }
                            { 1, 0.340001523, 0.409994662, 0.620353639 }
                            { 1, 0.340001523, 0.409994662, 0.0954390243 }
                            { 1, 0.340001523, 0.409994662, 0 }
                        }
                    }
                }
                Pass: i16 = -1
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 250, 400, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0434782617
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 0.5, 0 }
                            { 1, 1, 0 }
                            { 0.430107534, 0.430107534, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_W_bigglow02.dds"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                ParticleLinger: option[f32] = {
                    1.5
                }
                Lifetime: option[f32] = {
                    5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "dissolveAdd"
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 1, 0 }
                }
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 10 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.00416666688
                            0.127048612
                            0.224079862
                            0.287499994
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x4dbd1600: embed = ValueVector3 {
                        ConstantValue: vec3 = { 0, 1, 0 }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 0.400000006
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.0235294122, 0.545098066, 0.501960814, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.181222409
                            0.602787316
                            0.779662967
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0, 0, 0.0289054811, 0.122807018 }
                            { 0, 0.185974628, 0.153540939, 0.754385948 }
                            { 0, 0.545098066, 0.501960814, 1 }
                            { 0.0235294122, 0.545098066, 0.501960814, 0 }
                        }
                    }
                }
                Pass: i16 = 5
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.126412645
                                0.558626473
                                0.800000012
                            }
                            Values: list[f32] = {
                                0
                                0.332005024
                                0.734293103
                                1
                            }
                        }
                    }
                    ErosionSliceWidth: f32 = 1.20000005
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_R_Ground_A_Errode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                DepthBiasFactors: vec2 = { -1, -10 }
                DisableBackfaceCull: bool = true
                ParticleIsLocalOrientation: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.0129032256
                            0.35190919
                            0.994000018
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.5, 1.25, 1.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/common_color-hold.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                EmitterUvScrollRate: vec2 = { 0, -1 }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 2, 2 }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 8
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                ParticleLinger: option[f32] = {
                    2
                }
                Lifetime: option[f32] = {
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "FlatUnderDark1"
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 2, 0 }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Flags: u8 = 1
                    Radius: f32 = 100
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 10, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 0.379995435, 0.420004576, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0145161292
                            0.778032064
                            0.821510315
                            0.954233408
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0.379995435, 0.420004576, 0 }
                            { 0, 0.379995435, 0.420004576, 1 }
                            { 0, 0.379995435, 0.420004576, 1 }
                            { 0, 0.379995435, 0.420004576, 0.912280679 }
                            { 0, 0.379995435, 0.420004576, 0.140350878 }
                            { 0, 0.379995435, 0.420004576, 0 }
                        }
                    }
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.150000006
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.200000003
                    ErosionFeatherOut: f32 = 0.300000012
                    ErosionSliceWidth: f32 = 1.70000005
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_W_SmokeErode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 20, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 20, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 400, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0434782617
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 0.5, 0 }
                            { 1, 1, 0 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_darkFuzz.dds"
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_Mult.dds"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0.200000003, 0.200000003 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { -0.5, -0.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 400
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "brightTrailFlat1"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -200 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 0.5 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x6b77a8ca: embed = ValueColor {
                        Dynamics: pointer = VfxAnimatedColorVariableData {
                            Times: list[f32] = {
                                0.0107858246
                                0.990755022
                            }
                            Values: list[vec4] = {
                                { 1, 1, 1, 1 }
                                { 1, 1, 1, 1 }
                            }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 200, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.0126126129
                            0.502702713
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 0.149019614, 0.141176477, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0478087664
                            0.348391324
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0.149019614, 0.141176477, 0 }
                            { 0, 0.149019614, 0.141176477, 1 }
                            { 0, 0.149019614, 0.141176477, 1 }
                            { 0, 0.149019614, 0.141176477, 0 }
                        }
                    }
                }
                Pass: i16 = 9
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 260, 2, 2 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Cast_Trail.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                }
                EmitterUvScrollRate: vec2 = { -0.800000012, 0 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.25
                }
                ParticleLinger: option[f32] = {
                    10.1999998
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "flash"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { -30, 150, 0 }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.14549388
                            0.246432841
                            0.535211265
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.990291238, 0.990291238, 0.990291238, 0.990291238 }
                            { 0.990291238, 0.990291238, 0.990291238, 0.470135838 }
                            { 1, 1, 1, 0.0995628834 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 17
                DepthBiasFactors: vec2 = { 0, 4 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 250, 250, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.128600642
                            0.335680753
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.521604896, 0.521604896, 0.521604896 }
                            { 0.243421048, 0.26002413, 0.26002413 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_Flash.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 1, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.5
                }
                ParticleLinger: option[f32] = {
                    2
                }
                Lifetime: option[f32] = {
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "FlatUnderBright"
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 2, 0 }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Flags: u8 = 1
                    Radius: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0722673312
                            0.168629646
                            0.535211265
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 0.990291238, 0.990291238, 0.516607046 }
                            { 0.990291238, 0.990291238, 0.990291238, 0.224521801 }
                            { 1, 1, 1, 0.0995628834 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 17
                DepthBiasFactors: vec2 = { 0, 4 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 250, 400, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0434782617
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 0.5, 0 }
                            { 1, 1, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_W_bigglow02.dds"
            }
            VfxEmitterDefinitionData {
                EmitterName: string = "HIDE"
                Disabled: bool = true
                MaterialOverrideDefinitions: list[embed] = {
                    VfxMaterialOverrideDefinitionData {
                        Priority: i32 = 1
                        OverrideBlendMode: u32 = 2
                        BaseTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Base_empty32.dds"
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                ParticleLinger: option[f32] = {
                    11
                }
                Lifetime: option[f32] = {
                    8
                }
                IsSingleParticle: flag = true
                EmitterLinger: option[f32] = {
                    2
                }
                EmitterName: string = "Body"
                Disabled: bool = true
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xc1abfc9e
                            "HEAD"
                        }
                    }
                }
                BlendMode: u8 = 1
                Pass: i16 = 6
                ParticleIsLocalOrientation: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 180, 0 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Mordekaiser_Base_TX_CM.dds"
                EmitterUvScrollRate: vec2 = { 0, -1 }
            }
            VfxEmitterDefinitionData {
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 8
                }
                ParticleLinger: option[f32] = {
                    11
                }
                Lifetime: option[f32] = {
                    3
                }
                IsSingleParticle: flag = true
                EmitterLinger: option[f32] = {
                    2
                }
                EmitterName: string = "Dissolve1"
                Disabled: bool = true
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 1, 0 }
                }
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 10 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.00416666688
                            0.127048612
                            0.224079862
                            0.287499994
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x4dbd1600: embed = ValueVector3 {
                        ConstantValue: vec3 = { 0, 1, 0 }
                    }
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xc1abfc9e
                            "HEAD"
                        }
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.484693885
                            0.843792498
                            0.949999988
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 6
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.0893213004
                                0.241153926
                                0.482241362
                                0.946254849
                            }
                            Values: list[f32] = {
                                0
                                0.253361613
                                0.584722757
                                0.831500292
                                1
                            }
                        }
                    }
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_R_Ground_A_Errode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                ParticleIsLocalOrientation: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 180, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.0129032256
                            0.113056853
                            0.176419348
                            0.223430246
                            0.994000018
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.14999998, 1.25, 1.14999998 }
                            { 1.20000005, 0.912500024, 1.20000005 }
                            { 1.20000005, 0.0125000002, 1.20000005 }
                            { 1.20000005, 0, 1.20000005 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Mordekaiser_Base_TX_CM.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
                EmitterUvScrollRate: vec2 = { 0, -1 }
            }
        }
        ParticleName: string = "Mordekaiser_Base_Spawn"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Spawn"
        Flags: u16 = 198
    }
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_W_footstep" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.200000003
                }
                Lifetime: option[f32] = {
                    1.34500003
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Hit_Distort1"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 1, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    ScaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_color-heatbell.dds"
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 150
                DistortionDefinition: pointer = VfxDistortionDefinitionData {
                    Distortion: f32 = 0.0299999993
                    NormalMapTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_W_Footstep_Dist.dds"
                }
                DepthBiasFactors: vec2 = { -1, -4 }
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 90, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 150, 100, 100 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.130283222
                            0.400871456
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.565217376, 0.565217376, 0.565217376 }
                            { 1.03260875, 1.02263188, 1.02263188 }
                            { 1.25, 1.25, 1.25 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_W_Footstep_Dist_A.dds"
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_W_Footstep_Dist_A.dds"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 20
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    11
                }
                Lifetime: option[f32] = {
                    0.400000006
                }
                IsSingleParticle: flag = true
                EmitterName: string = "blast1"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 400, 0, 400 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    12
                                }
                                KeyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 400, 0, 400 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 0, 5 }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, 15, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 15, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Radius: f32 = 60
                    Height: f32 = 1
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.76000613, 0.689997733, 0.530006886, 0.600000024 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.76000613, 0.689997733, 0.530006886, 0 }
                            { 0.76000613, 0.689997733, 0.530006886, 0.600000024 }
                            { 0.684011281, 0.621003211, 0.47701022, 0.401995867 }
                            { 0.76000613, 0.689997733, 0.530006886, 0 }
                        }
                    }
                }
                Pass: i16 = -150
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = 1.20000005
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.150000006
                                1
                            }
                            Values: list[f32] = {
                                0
                                1.20000005
                            }
                        }
                    }
                    ErosionFeatherOut: f32 = 0.200000003
                    ErosionSliceWidth: f32 = 1.70000005
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_W_SmokeErode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 90, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 90, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 50, 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 50, 1, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 1, 1 }
                            { 1, 2, 2 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Sion_Skin05_Sl_Dust_01.dds"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.800000012
                                    1.29999995
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            5
                        }
                    }
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.800000012
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    11
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Rocks"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 1200, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.800000012
                                    1.29999995
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 100, 1200, 0 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 1, 0 }
                }
                Drag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 10, 0 }
                        }
                    }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -2500, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -2500, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Radius: f32 = 60
                    Height: f32 = 1
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    ScaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.200000003
                            0.899999976
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 10
                AlphaRef: u8 = 60
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 4, 7, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.600000024
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.400000006
                                    0.800000012
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 4, 7, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        Values: list[vec3] = {
                            { 2, 1, 1 }
                            { 3, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_W_dirt_rock.dds"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
        }
        ParticleName: string = "Mordekaiser_Base_W_footstep"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_W_footstep"
    }
}
