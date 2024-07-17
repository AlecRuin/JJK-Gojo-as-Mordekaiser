#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_E_mis" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.449999988
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    1.20000005
                }
                IsSingleParticle: flag = true
                EmitterName: string = "surfaceRipples"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -150, 120 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Shockwave.scb"
                    }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.680003047 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.011009085
                            0.250669241
                            0.501170039
                            0.567551494
                            0.666575968
                            0.789416373
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.680003047 }
                            { 1, 1, 1, 0.584465444 }
                            { 1, 1, 1, 0.425125867 }
                            { 1, 1, 1, 0.202314958 }
                            { 1, 1, 1, 0.0509313568 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 12
                AlphaRef: u8 = 0
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                StencilRef: u8 = 2
                ParticleIsLocalOrientation: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -90, 0, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 0.800000012, 0.600000024 }
                            { 0.899999976, 0.100000001, 0.300000012 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Ground_ShockWave.dds"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.100000001, 0.100000001 }
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
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Ground_ShockWave.dds"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0.5, 0.5 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0.200000003, 0 }
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
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
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.400000006
                }
                ParticleLinger: option[f32] = {
                    2
                }
                Lifetime: option[f32] = {
                    0.200000003
                }
                IsSingleParticle: flag = true
                EmitterName: string = "BackGlow1"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -50, 100 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        Values: list[vec4] = {
                            { 0.0156862754, 0.513725519, 0.282352954, 0 }
                            { 0.278431386, 1, 0.858823538, 1 }
                            { 0, 0.164706007, 0.137254998, 0 }
                        }
                    }
                }
                Pass: i16 = -50
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 120, 120, 120 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        Values: list[vec3] = {
                            { 120, 120, 120 }
                            { 120, 60, 120 }
                            { 120, 24, 120 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 2, 1, 1 }
                            { 2, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yorick/Skins/Base/Particles/common_ball32_02.dds"
            }
        }
        ParticleName: string = "Mordekaiser_Base_E_mis"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_E_mis"
    }
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_R_Spirit_dark_inDreathRealm" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.5
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 10
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
                                    0.800000012
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
                Lifetime: option[f32] = {
                    9.5
                }
                EmitterName: string = "DARKMIST"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -10 }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -100 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, -100 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    Flags: u8 = 1
                    Size: vec3 = { 10, 10, 10 }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 200, 0 }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            -0.00738007389
                            0.127255216
                            0.983408451
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 0.31764707, 0.294117659, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00126742711
                            0.103393443
                            0.214542717
                            0.385573953
                            0.542878747
                            0.692089498
                            0.821419358
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0.31764707, 0.294117659, 0 }
                            { 0, 0.31764707, 0.293968409, 0.752519846 }
                            { 0, 0.31764707, 0.293805987, 1 }
                            { 0, 0.316533536, 0.293086588, 1 }
                            { 0, 0.315589398, 0.292212397, 0.785123944 }
                            { 0, 0.315021873, 0.291686922, 0.30578512 }
                            { 0, 0.31764707, 0.294117659, 0.105785139 }
                            { 0, 0.31764707, 0.294117659, 0 }
                        }
                    }
                }
                Pass: i16 = 7
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 100
                }
                DisableBackfaceCull: bool = true
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRandomStartFrame: flag = true
                IsRotationEnabled: flag = true
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
                        }
                        Values: list[vec3] = {
                            { 100, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 120, 35, 35 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 120, 0, 0 }
                            { 120, 0, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.185585588
                            0.618018031
                            1
                        }
                        Values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.400000006 }
                            { 0.649999976, 0.649943113, 0.649943113 }
                            { 0.909105241, 0.909402549, 0.909402549 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_Wispy.dds"
                NumFrames: u16 = 8
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
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
                TimeBeforeFirstEmission: f32 = 2
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 2.5
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 8.5
                }
                Lifetime: option[f32] = {
                    8.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "spotlightGround"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.100007631 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00179211469
                            0.0819214657
                            0.885370791
                            0.996415794
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.0119412094 }
                            { 1, 1, 1, 0.0992386863 }
                            { 1, 1, 1, 0.100007631 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                MiscRenderFlags: u8 = 1
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 90, 1 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Z_SoftSphere.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.699999988
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 3
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.5
                }
                Lifetime: option[f32] = {
                    9
                }
                EmitterName: string = "coreGlow"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 200, 0 }
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
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            -0.0137524558
                            0.990176797
                        }
                        Values: list[vec4] = {
                            { 0.510002315, 1, 0.919996977, 1 }
                            { 0.510002315, 1, 0.919996977, 0 }
                        }
                    }
                }
                Pass: i16 = 20
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 0, 0 }
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
                        }
                        Values: list[vec3] = {
                            { 200, 0, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 140, 50, 50 }
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
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 140, 50, 50 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.46393761
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_Flash.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 1.5
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 2.5
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 8.5
                }
                Lifetime: option[f32] = {
                    8.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "darkBack"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 200, 0 }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.00784313772, 0.188235298, 0.172549024, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00179211469
                            0.0819214657
                            0.885370791
                            0.996415794
                        }
                        Values: list[vec4] = {
                            { 0.00784313772, 0.188235298, 0.172549024, 0.119402982 }
                            { 0.00784313772, 0.188235298, 0.172549024, 0.99231118 }
                            { 0.00784313772, 0.188235298, 0.172549024, 1 }
                            { 0.00784313772, 0.188235298, 0.172549024, 0 }
                        }
                    }
                }
                Pass: i16 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 80, 60, 1 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/common_Aura_Self.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
        }
        ParticleName: string = "Mordekaiser_Base_R_Spirit_dark_inDreathRealm"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_R_Spirit_dark_inDreathRealm"
        Flags: u16 = 132
    }
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_R_SoulTeather" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.200000003
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                ParticleLinger: option[f32] = {
                    1.5
                }
                EmitterName: string = "DarkBeam"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 50, 200, 0 }
                }
                Primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 0, 600, 0 }
                        }
                        mLocalSpaceTargetOffset: vec3 = { 0, -20, 0 }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 0.101960786, 0.117647059, 1 }
                }
                ColorLookUpScales: vec2 = { 1, 0.200000003 }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 1, 1 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_SoulTether.dds"
                StartFrame: u16 = 1
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { -1, 0 }
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_SoulTetherMult.dds"
                    TexAddressModeMult: u8 = 2
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 0.300000012 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 0.600000024 }
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, -1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.200000003
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                ParticleLinger: option[f32] = {
                    1.5
                }
                EmitterName: string = "BrightbBeam"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 50, 200, 0 }
                }
                Primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 0, 600, 0 }
                        }
                        mAnimatedColorWithDistance: embed = ValueColor {
                            Dynamics: pointer = VfxAnimatedColorVariableData {
                                Times: list[f32] = {
                                    0
                                    1
                                }
                                Values: list[vec4] = {
                                    { 1, 1, 1, 1 }
                                    { 1, 1, 1, 1 }
                                }
                            }
                        }
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.00392156886, 0.952941179, 1, 1 }
                }
                Pass: i16 = 1
                ColorLookUpScales: vec2 = { 1, 0.200000003 }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 1, 1 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_SoulTether.dds"
                StartFrame: u16 = 1
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { -1, 0 }
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_SoulTetherMult.dds"
                    TexAddressModeMult: u8 = 2
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 0.300000012 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 0.600000024 }
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, -1 }
                    }
                }
            }
        }
        VisibilityRadius: f32 = 5000
        ParticleName: string = "Mordekaiser_Base_R_SoulTeather"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_R_SoulTeather"
        Flags: u16 = 132
    }
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_R_Spirit_bright_inDreathRealm" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 1.25
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 10
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            2
                        }
                    }
                }
                Lifetime: option[f32] = {
                    9.5
                }
                EmitterName: string = "brightMist"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -10, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -10, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Flags: u8 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 200, 0 }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.400000006 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00126742711
                            0.140443206
                            0.266090214
                            0.385573953
                            0.542878747
                            0.692089498
                            0.821419358
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.294396371 }
                            { 1, 0.998203158, 0.998203158, 0.400000006 }
                            { 1, 0.996494412, 0.996494412, 0.400000006 }
                            { 0.991735518, 0.993522108, 0.993522108, 0.314049602 }
                            { 0.991735518, 0.991735518, 0.991735518, 0.122314051 }
                            { 1, 1, 1, 0.0423140526 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                DisableBackfaceCull: bool = true
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRandomStartFrame: flag = true
                IsRotationEnabled: flag = true
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
                        }
                        Values: list[vec3] = {
                            { 100, 0, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 160, 35, 35 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 160, 35, 35 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0258064531
                            0.127419353
                            0.406451613
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.673462927, 0.675678372, 0.675678372 }
                            { 0.378773004, 0.378798574, 0.378798574 }
                            { 0.200000003, 0.200000003, 0.200000003 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_Wispy.dds"
                NumFrames: u16 = 8
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
                TimeBeforeFirstEmission: f32 = 1
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 9.5
                }
                Lifetime: option[f32] = {
                    1.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "OverGlow"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 200, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_alpha_02.dds"
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 1, 0.933333337, 0.156862751 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.161883146
                            0.973386168
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 1, 0.933333337, 0.156862751 }
                            { 0, 1, 0.933333337, 0.156862751 }
                            { 0, 1, 0.933333337, 0.156862751 }
                            { 0, 1, 0.933333337, 0.156862751 }
                        }
                    }
                }
                Pass: i16 = 1
                MeshRenderFlags: u8 = 0
                DisableBackfaceCull: bool = true
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 80, 1, 1 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Z_SoftSphere.dds"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 1.25
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                Lifetime: option[f32] = {
                    9.5
                }
                ChildParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    ChildrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            EffectKey: hash = "Mordekaiser_R_Spirit_HeartBeat_inDeathRealm"
                        }
                    }
                }
                EmitterName: string = "HeartbeatParent"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 200, 0 }
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
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            -0.0137524558
                            0.990176797
                        }
                        Values: list[vec4] = {
                            { 0.510002315, 1, 0.919996977, 1 }
                            { 0.510002315, 1, 0.919996977, 0 }
                        }
                    }
                }
                Pass: i16 = 20
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 160, 100, 100 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/common_Black.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 4, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.25
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 3
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.5
                }
                Lifetime: option[f32] = {
                    9
                }
                EmitterName: string = "coreGlow"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 200, 0 }
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
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            -0.0137524558
                            0.990176797
                        }
                        Values: list[vec4] = {
                            { 0.510002315, 1, 0.919996977, 1 }
                            { 0.510002315, 1, 0.919996977, 0 }
                        }
                    }
                }
                Pass: i16 = 20
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 0, 0 }
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
                        }
                        Values: list[vec3] = {
                            { 200, 0, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 40, 50, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.46393761
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_Flash.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 4, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 2
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 2.5
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 8.5
                }
                Lifetime: option[f32] = {
                    8.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "spotlightGround"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.100007631 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00179211469
                            0.0819214657
                            0.885370791
                            0.996415794
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.0119412094 }
                            { 1, 1, 1, 0.0992386863 }
                            { 1, 1, 1, 0.100007631 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                MiscRenderFlags: u8 = 1
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 90, 1 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Z_SoftSphere.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
            }
        }
        ParticleName: string = "Mordekaiser_Base_R_Spirit_bright_inDreathRealm"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_R_Spirit_bright_inDreathRealm"
        Flags: u16 = 132
    }
}
