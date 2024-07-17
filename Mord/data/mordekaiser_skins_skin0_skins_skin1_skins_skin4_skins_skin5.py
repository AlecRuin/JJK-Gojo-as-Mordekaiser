#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_R_Spirit_Morde_Enemy" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.800000012
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2.5
                }
                Lifetime: option[f32] = {
                    8.5
                }
                EmitterName: string = "Breathing"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 0, 200 }
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
                    ConstantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00179211469
                            0.103942655
                            0.386508226
                            0.55138278
                            0.727010012
                            0.890681028
                            0.996415794
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.0955223888 }
                            { 1, 1, 1, 0.238805965 }
                            { 1, 1, 1, 0.705965042 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 1, 1, 0.625925303 }
                            { 1, 1, 1, 0.238805965 }
                            { 1, 1, 1, 0.0955223888 }
                        }
                    }
                }
                Pass: i16 = 20
                DepthBiasFactors: vec2 = { 1, 9 }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 80, 60, 60 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.11469534
                            0.333333343
                            0.5
                            0.655913949
                            0.879928291
                            1
                        }
                        Values: list[vec3] = {
                            { 0.135294124, 0.135294124, 0.135294124 }
                            { 0.252941191, 0.256504297, 0.232974887 }
                            { 0.852941155, 0.832658648, 0.832658648 }
                            { 1, 1, 1 }
                            { 0.835294127, 0.829074442, 0.829074442 }
                            { 0.329411775, 0.31762597, 0.31762597 }
                            { 0.129411772, 0.129411772, 0.129411772 }
                        }
                    }
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
                TimeBeforeFirstEmission: f32 = 0.25
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
                    ConstantValue: vec3 = { 0, 0, 200 }
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
                    ConstantValue: vec4 = { 0.458823532, 0.458823532, 0.458823532, 1 }
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
                            { 0.458823532, 0.458823532, 0.458823532, 0 }
                            { 0.458823532, 0.458823532, 0.458590716, 0.752519846 }
                            { 0.458823532, 0.458823532, 0.458337307, 1 }
                            { 0.458823532, 0.457215101, 0.457215101, 1 }
                            { 0.455031604, 0.455851346, 0.455851346, 0.785123944 }
                            { 0.455031604, 0.455031604, 0.455031604, 0.30578512 }
                            { 0.458823532, 0.458823532, 0.458823532, 0.105785139 }
                            { 0.458823532, 0.458823532, 0.458823532, 0 }
                        }
                    }
                }
                Pass: i16 = 8
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 100
                }
                DepthBiasFactors: vec2 = { 1, 7 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
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
                    ConstantValue: vec3 = { 110, 35, 35 }
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
                            { 110, 0, 0 }
                            { 110, 0, 0 }
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
                TimeBeforeFirstEmission: f32 = 0.5
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 400
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                Lifetime: option[f32] = {
                    9.5
                }
                EmitterName: string = "DarkTrailFlat"
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
                    EmitOffset: vec3 = { 0, 0, 200 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.13333334, 0.13333334, 0.13333334, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.172290087
                            0.334661365
                            1
                        }
                        Values: list[vec4] = {
                            { 0.13333334, 0.13333334, 0.13333334, 0 }
                            { 0.13333334, 0.13333334, 0.13333334, 1 }
                            { 0.13333334, 0.13333334, 0.13333334, 1 }
                            { 0.13333334, 0.13333334, 0.13333334, 0 }
                        }
                    }
                }
                Pass: i16 = 1
                AlphaRef: u8 = 0
                DepthBiasFactors: vec2 = { 1, 1 }
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 130, 2, 2 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Cast_Trail.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                }
                EmitterUvScrollRate: vec2 = { -0.800000012, 0 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 2
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 12
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.20000005
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                Lifetime: option[f32] = {
                    9.5
                }
                FieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    FieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            Radius: embed = ValueFloat {
                                ConstantValue: f32 = 200
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
                    ConstantValue: vec3 = { 0, 5, 5 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
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
                            { 0, 5, 5 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 3 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 30, 0, 10 }
                        Dynamics: pointer = VfxAnimatedVector3fVariableData {
                            ProbabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    KeyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    KeyValues: list[f32] = {
                                        0.899999976
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
                            Values: list[vec3] = {
                                { 30, 0, 10 }
                            }
                        }
                    }
                    EmitRotationAngles: list[embed] = {
                        ValueFloat {
                            ConstantValue: f32 = 1
                            Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                Times: list[f32] = {
                                    0
                                }
                                Values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            ConstantValue: f32 = 1
                        }
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                        { 90, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 200 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Veigar/Skins/Base/Particles/common_color-smoke32_07.dds"
                BlendMode: u8 = 2
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.0202702694
                            0.123123124
                            0.997747719
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 3
                MeshRenderFlags: u8 = 0
                ColorRenderFlags: u8 = 1
                DepthBiasFactors: vec2 = { 1, 4 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
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
                    ConstantValue: vec3 = { 3, 3, 3 }
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
                            0.0272191986
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 3, 3, 3 }
                            { 0, 0, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 6, 6, 6 }
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
                TimeBeforeFirstEmission: f32 = 2
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 8.5
                }
                Lifetime: option[f32] = {
                    2.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Shadow"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 0, 2 }
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
                    ConstantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.145529032
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.600000024 }
                        }
                    }
                }
                MiscRenderFlags: u8 = 1
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 150, 0 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_R_spotLight.dds"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 1.5
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
                    ConstantValue: vec3 = { 0, 0, 200 }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
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
                            { 1, 1, 1, 0.735990942 }
                            { 1, 0.998203158, 0.998203158, 1 }
                            { 1, 0.996494412, 0.996494412, 1 }
                            { 0.991735518, 0.993522108, 0.993522108, 0.785123944 }
                            { 0.991735518, 0.991735518, 0.991735518, 0.30578512 }
                            { 1, 1, 1, 0.105785139 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 9
                DepthBiasFactors: vec2 = { 1, 8 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRandomStartFrame: flag = true
                IsRotationEnabled: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
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
                            { 90, 0, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 35, 35 }
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
                            0.11981982
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 200, 0, 0 }
                            { 200, 0, 0 }
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
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 9.5
                }
                Lifetime: option[f32] = {
                    2.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "darkGloBak"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Flags: u8 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 200 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_alpha_02.dds"
                BlendMode: u8 = 2
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.910002291, 0.970000744, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0692307726
                            0.97499907
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.910002291, 0.970000744, 0 }
                            { 1, 0.910002291, 0.970000744, 1 }
                            { 1, 0.910002291, 0.970000744, 1 }
                            { 1, 0.910002291, 0.970000744, 1 }
                        }
                    }
                }
                Pass: i16 = 6
                MeshRenderFlags: u8 = 0
                DepthBiasFactors: vec2 = { 1, 5 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 130, 1, 1 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Z_SoftSphere.dds"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 1
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 15
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
                EmitterName: string = "darkMistLinger"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -100, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    Flags: u8 = 1
                    Size: vec3 = { 10, 10, 10 }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 200 }
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
                    ConstantValue: vec4 = { 0.396078438, 0.396078438, 0.396078438, 1 }
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
                            { 0.396078438, 0.396078438, 0.396078438, 0 }
                            { 0.396078438, 0.396078438, 0.395877451, 0.752519846 }
                            { 0.396078438, 0.396078438, 0.395658702, 1 }
                            { 0.396078438, 0.394689947, 0.394689947, 1 }
                            { 0.39280507, 0.393512696, 0.393512696, 0.785123944 }
                            { 0.39280507, 0.39280507, 0.39280507, 0.30578512 }
                            { 0.396078438, 0.396078438, 0.396078438, 0.105785139 }
                            { 0.396078438, 0.396078438, 0.396078438, 0 }
                        }
                    }
                }
                Pass: i16 = 7
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 100
                }
                DepthBiasFactors: vec2 = { 1, 6 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
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
                    ConstantValue: vec3 = { 120, 35, 35 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 120, 35, 35 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.14054054
                            0.581981957
                            1
                        }
                        Values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.400000006 }
                            { 0.616947353, 0.617325723, 0.617325723 }
                            { 0.878947377, 0.878947377, 0.878947377 }
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
                EmitterName: string = "lightGloBack"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 0, 200 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.200000003 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00179211469
                            0.0819214657
                            0.885370791
                            0.996415794
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.0238805972 }
                            { 1, 1, 1, 0.198462233 }
                            { 1, 1, 1, 0.200000003 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 2
                DepthBiasFactors: vec2 = { 1, 2 }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 120, 1, 1 }
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
                TimeBeforeFirstEmission: f32 = 0.600000024
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 20
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.20000005
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    3
                }
                Lifetime: option[f32] = {
                    8.5
                }
                EmitterName: string = "tendrils1"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 40 }
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
                                    1
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 40 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 1, 0, 1 }
                    }
                    EmitRotationAngles: list[embed] = {
                        ValueFloat {
                            ConstantValue: f32 = 360
                            Dynamics: pointer = VfxAnimatedFloatVariableData {
                                ProbabilityTables: list[pointer] = {
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
                                    0
                                }
                                Values: list[f32] = {
                                    360
                                }
                            }
                        }
                        ValueFloat {
                            ConstantValue: f32 = 90
                        }
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 1, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 200 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_Cast_Tendrils.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.235294119, 0.235294119, 0.235294119, 1 }
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
                DepthBiasFactors: vec2 = { 1, 3 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsDirectionOriented: flag = true
                HasPostRotateOrientation: flag = true
                IsRandomStartFrame: flag = true
                IsRotationEnabled: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 45, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.800000012, 0.800000012, 0.300000012 }
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
                            0.100000001
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.800000012, 0.800000012, 0.300000012 }
                            { 0.800000012, 0.800000012, 0.300000012 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.156117409
                            0.368129104
                            0.58348316
                            0.745442212
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1.32907796 }
                            { 1, 1, 2.51376462 }
                            { 1, 1, 2.26330853 }
                            { 1, 1, 1.40607905 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_Tendrils.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
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
        }
        ParticleName: string = "Mordekaiser_Base_R_Spirit_Morde_Enemy"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_R_Spirit_Morde_Enemy"
        Flags: u16 = 132
    }
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_R_Spirit_Morde" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.200000003
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
                    ConstantValue: vec3 = { 0, 150, 0 }
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
                    ConstantValue: vec4 = { 0.215686277, 0.215686277, 0.215686277, 1 }
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
                            { 0.215686277, 0.215686277, 0.215686277, 0 }
                            { 0.215686277, 0.215686277, 0.215576828, 0.752519846 }
                            { 0.215686277, 0.215686277, 0.215457708, 1 }
                            { 0.215686277, 0.214930162, 0.214930162, 1 }
                            { 0.21390374, 0.214289084, 0.214289084, 0.785123944 }
                            { 0.21390374, 0.21390374, 0.21390374, 0.30578512 }
                            { 0.215686277, 0.215686277, 0.215686277, 0.105785139 }
                            { 0.215686277, 0.215686277, 0.215686277, 0 }
                        }
                    }
                }
                Pass: i16 = 8
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 100
                }
                DepthBiasFactors: vec2 = { 1, 7 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
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
                    ConstantValue: vec3 = { 180, 35, 35 }
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
                            { 180, 0, 0 }
                            { 180, 0, 0 }
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
                TimeBeforeFirstEmission: f32 = 0.5
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
                    ConstantValue: vec3 = { 0, 100, 0 }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.489997715 }
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
                            { 1, 1, 1, 0.36063388 }
                            { 1, 0.998203158, 0.998203158, 0.489997715 }
                            { 1, 0.996494412, 0.996494412, 0.489997715 }
                            { 0.991735518, 0.993522108, 0.993522108, 0.384708941 }
                            { 0.991735518, 0.991735518, 0.991735518, 0.149834007 }
                            { 1, 1, 1, 0.0518344752 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 9
                DepthBiasFactors: vec2 = { 1, 8 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRandomStartFrame: flag = true
                IsRotationEnabled: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
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
                            { 90, 0, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 180, 35, 35 }
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
                            0.11981982
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 180, 0, 0 }
                            { 180, 0, 0 }
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
                TimeBeforeFirstEmission: f32 = 0.5
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 9.5
                }
                Lifetime: option[f32] = {
                    2.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "darkGloBak"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Flags: u8 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 100, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_alpha_02.dds"
                BlendMode: u8 = 2
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.910002291, 0.970000744, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0692307726
                            0.97499907
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.910002291, 0.970000744, 0 }
                            { 1, 0.910002291, 0.970000744, 1 }
                            { 1, 0.910002291, 0.970000744, 1 }
                            { 1, 0.910002291, 0.970000744, 1 }
                        }
                    }
                }
                Pass: i16 = 6
                MeshRenderFlags: u8 = 0
                DepthBiasFactors: vec2 = { 1, 5 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 130, 1, 1 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Z_SoftSphere.dds"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.5
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
                EmitterName: string = "lightGloBack"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 100, 0 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.200000003 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00179211469
                            0.0819214657
                            0.885370791
                            0.996415794
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.0238805972 }
                            { 1, 1, 1, 0.198462233 }
                            { 1, 1, 1, 0.200000003 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 2
                DepthBiasFactors: vec2 = { 1, 2 }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 120, 1, 1 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Z_SoftSphere.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.800000012
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2.5
                }
                Lifetime: option[f32] = {
                    8.5
                }
                EmitterName: string = "Breathing"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 150, 0 }
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
                    ConstantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00179211469
                            0.103942655
                            0.386508226
                            0.55138278
                            0.727010012
                            0.890681028
                            0.996415794
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.0955223888 }
                            { 1, 1, 1, 0.238805965 }
                            { 1, 1, 1, 0.705965042 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 1, 1, 0.625925303 }
                            { 1, 1, 1, 0.238805965 }
                            { 1, 1, 1, 0.0955223888 }
                        }
                    }
                }
                Pass: i16 = 20
                DepthBiasFactors: vec2 = { 1, 9 }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 60, 60, 60 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.11469534
                            0.333333343
                            0.5
                            0.655913949
                            0.879928291
                            1
                        }
                        Values: list[vec3] = {
                            { 0.135294124, 0.135294124, 0.135294124 }
                            { 0.252941191, 0.256504297, 0.232974887 }
                            { 0.852941155, 0.832658648, 0.832658648 }
                            { 1, 1, 1 }
                            { 0.835294127, 0.829074442, 0.829074442 }
                            { 0.329411775, 0.31762597, 0.31762597 }
                            { 0.129411772, 0.129411772, 0.129411772 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Z_SoftSphere.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.5
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 400
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                Lifetime: option[f32] = {
                    9.5
                }
                EmitterName: string = "DarkTrailFlat"
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
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 100, 0 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.13333334, 0.13333334, 0.13333334, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.172290087
                            0.334661365
                            1
                        }
                        Values: list[vec4] = {
                            { 0.13333334, 0.13333334, 0.13333334, 0 }
                            { 0.13333334, 0.13333334, 0.13333334, 1 }
                            { 0.13333334, 0.13333334, 0.13333334, 1 }
                            { 0.13333334, 0.13333334, 0.13333334, 0 }
                        }
                    }
                }
                Pass: i16 = 1
                AlphaRef: u8 = 0
                DepthBiasFactors: vec2 = { 1, 1 }
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 130, 2, 2 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Cast_Trail.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 1, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                }
                EmitterUvScrollRate: vec2 = { -0.800000012, 0 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 2
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 12
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.20000005
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                Lifetime: option[f32] = {
                    9.5
                }
                FieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    FieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            Radius: embed = ValueFloat {
                                ConstantValue: f32 = 200
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
                    ConstantValue: vec3 = { 0, 5, 5 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
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
                            { 0, 5, 5 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 3 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 30, 0, 10 }
                        Dynamics: pointer = VfxAnimatedVector3fVariableData {
                            ProbabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    KeyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    KeyValues: list[f32] = {
                                        0.899999976
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
                            Values: list[vec3] = {
                                { 30, 0, 10 }
                            }
                        }
                    }
                    EmitRotationAngles: list[embed] = {
                        ValueFloat {
                            ConstantValue: f32 = 1
                            Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                Times: list[f32] = {
                                    0
                                }
                                Values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            ConstantValue: f32 = 1
                        }
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                        { 90, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 100, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Veigar/Skins/Base/Particles/common_color-smoke32_07.dds"
                BlendMode: u8 = 2
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.0202702694
                            0.123123124
                            0.997747719
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 3
                MeshRenderFlags: u8 = 0
                ColorRenderFlags: u8 = 1
                DepthBiasFactors: vec2 = { 1, 4 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
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
                    ConstantValue: vec3 = { 3, 3, 3 }
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
                            0.0272191986
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 3, 3, 3 }
                            { 0, 0, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 6, 6, 6 }
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
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 15
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
                EmitterName: string = "darkMistLinger"
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -100, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    Flags: u8 = 1
                    Size: vec3 = { 10, 10, 10 }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 100, 0 }
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
                    ConstantValue: vec4 = { 0.223529413, 0.223529413, 0.223529413, 1 }
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
                            { 0.223529413, 0.223529413, 0.223529413, 0 }
                            { 0.223529413, 0.223529413, 0.223415986, 0.752519846 }
                            { 0.223529413, 0.223529413, 0.223292544, 1 }
                            { 0.223529413, 0.222745806, 0.222745806, 1 }
                            { 0.221682057, 0.222081423, 0.222081423, 0.785123944 }
                            { 0.221682057, 0.221682057, 0.221682057, 0.30578512 }
                            { 0.223529413, 0.223529413, 0.223529413, 0.105785139 }
                            { 0.223529413, 0.223529413, 0.223529413, 0 }
                        }
                    }
                }
                Pass: i16 = 7
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 100
                }
                DepthBiasFactors: vec2 = { 1, 6 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
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
                    ConstantValue: vec3 = { 120, 35, 35 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 120, 35, 35 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.14054054
                            0.581981957
                            1
                        }
                        Values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.400000006 }
                            { 0.616947353, 0.617325723, 0.617325723 }
                            { 0.878947377, 0.878947377, 0.878947377 }
                            { 1, 1, 1 }
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
                TimeBeforeFirstEmission: f32 = 0.5
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 8.5
                }
                Lifetime: option[f32] = {
                    2.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Shadow"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 0, 2 }
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
                    ConstantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.145529032
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.600000024 }
                        }
                    }
                }
                MiscRenderFlags: u8 = 1
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 90 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 150, 0 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_R_spotLight.dds"
            }
        }
        ParticleName: string = "Mordekaiser_Base_R_Spirit_Morde"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_R_Spirit_Morde"
        Flags: u16 = 140
    }
}
