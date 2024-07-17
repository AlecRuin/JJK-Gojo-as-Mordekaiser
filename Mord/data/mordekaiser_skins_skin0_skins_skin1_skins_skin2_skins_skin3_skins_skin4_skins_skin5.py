#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Passive_Dance_Fireworks" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.649999976
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 6
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
                                    0.800000012
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
                Lifetime: option[f32] = {
                    3
                }
                EmitterName: string = "SMOKE"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 500, 2 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 500, 2 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 1, 0 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
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
                                            -5
                                            5
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
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 80 }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00126742711
                            0.103393443
                            0.214542717
                            0.385573953
                            0.539355874
                            0.681520879
                            0.821419358
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0, 0, 0 }
                            { 1, 0.450980395, 0, 0.376476347 }
                            { 0.784313738, 0.490196079, 0.0156862754, 0.500007629 }
                            { 0.43921569, 0.0509803928, 0, 0.500007629 }
                            { 0.392156869, 0, 0.286274523, 0.392162859 }
                            { 0.260504216, 0.00784313772, 0.2997199, 0.152943507 }
                            { 0.145098045, 0.192156866, 0.250980407, 0.0529419854 }
                            { 0.149019614, 0.149019614, 0.149019614, 0 }
                        }
                    }
                }
                Pass: i16 = -1
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 100
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
                    ErosionFeatherOut: f32 = 0.200000003
                    ErosionSliceWidth: f32 = 1.70000005
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_I_SmokeErode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 150, 0, 0 }
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
                            { 150, 0, 0 }
                        }
                    }
                }
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
                        }
                        Values: list[vec3] = {
                            { 200, 35, 35 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.996472657
                        }
                        Values: list[vec3] = {
                            { 0.400000006, 0, 0 }
                            { 1, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Morde_Skin03_Dust.dds"
                NumFrames: u16 = 8
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.649999976
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 3
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.39999998
                }
                ParticleLinger: option[f32] = {
                    0.200000003
                }
                Lifetime: option[f32] = {
                    2.5
                }
                EmitterName: string = "firePillar"
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 5, 0, -80 }
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
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_Smoke_A.scb"
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.56078434, 0.368627459, 0.172549024, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0201869775
                            0.815241039
                            1
                        }
                        Values: list[vec4] = {
                            { 0.56078434, 0.368627459, 0.172549024, 0 }
                            { 0.56078434, 0.368627459, 0.172549024, 1 }
                            { 0.56078434, 0.368627459, 0.172549024, 1 }
                            { 0.56078434, 0.368627459, 0.172549024, 0 }
                        }
                    }
                }
                AlphaRef: u8 = 0
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.150000006
                                0.725408375
                                0.78865701
                                0.930580735
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                                0.107954547
                                0.863636374
                                1
                            }
                        }
                    }
                    LingerErosionDriveCurve: embed = ValueFloat {
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
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_I_SmokeErode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                DisableBackfaceCull: bool = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 0, 0 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.5, 0.5, 0.200000003 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.699999988
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
                                    0.699999988
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0.5, 0.5, 0.200000003 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.110590294
                            0.243071362
                            0.408427328
                            0.998387098
                        }
                        Values: list[vec3] = {
                            { 0.257142872, 0.5, 0.257142872 }
                            { 0.449579835, 0.7313025, 0.449579835 }
                            { 0.628571451, 0.88277334, 0.631311536 }
                            { 0.79285717, 1, 0.79285717 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_W_Cast_Beam.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 4, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 1.25 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 1 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0, 1 }
                        }
                    }
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_Q_Mult.dds"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 1.5 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
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
                                    0.504901946
                                    0.83006537
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.200000003
                                    0.394285709
                                    0.628571451
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
                    8
                }
                IsSingleParticle: flag = true
                EmitterName: string = "FlameStartBright"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 400, 100 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 0, 0, 15 }
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
                                            -20
                                            20
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
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 80 }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.779995441 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00126742711
                            0.103393443
                            0.214542717
                            0.399009824
                            0.53392148
                            0.692089498
                            0.821419358
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0, 0, 0 }
                            { 1, 0.450980395, 0, 0.587290645 }
                            { 1, 0.773039222, 0.0980392173, 0.779995441 }
                            { 1, 1, 0, 0.779995441 }
                            { 0.996389627, 0.583700955, 0.101960786, 0.611761093 }
                            { 0.992156863, 0.41568628, 0.0784313753, 0.238586828 }
                            { 1, 0.360784322, 0.0666666701, 0.0825877488 }
                            { 1, 0.141176477, 0.0274509806, 0 }
                        }
                    }
                }
                Pass: i16 = 2
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 100
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
                    ErosionFeatherOut: f32 = 0.200000003
                    ErosionSliceWidth: f32 = 1.70000005
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_I_SmokeErode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 250, 0, 0 }
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
                            { 250, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 50, 35, 35 }
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
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 50, 35, 35 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0648113042
                            0.176558331
                            0.517793298
                            0.990196049
                        }
                        Values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 0.830168068, 0.830168068, 0.830168068 }
                            { 1.19151783, 1.19151783, 1.19151783 }
                            { 1.53035712, 1.53035712, 1.53035712 }
                            { 1.85000002, 1.85000002, 1.85000002 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_Q_Wispy.dds"
                NumFrames: u16 = 8
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 6, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.649999976
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 10
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.300000012
                }
                Lifetime: option[f32] = {
                    6
                }
                EmitterName: string = "MainFlash"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 50, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 40, 80 }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.843137264, 0.474509805, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.652482271
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.333333343
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0.0178571437
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.489361703
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            0.018253969
                            0.0694885403
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 0.843137264, 0.474509805, 1 }
                            { 1, 0.843137264, 0.474509805, 0.634146333 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 3
                AlphaRef: u8 = 0
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 120
                }
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 90 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 90, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 320, 150, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 320, 150, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_Q_Flash.dds"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.649999976
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 80
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.5
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    0.5
                }
                Lifetime: option[f32] = {
                    6
                }
                EmitterName: string = "Streaks"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 2000, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 2000, 0 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 3, 3, 3 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 0, 0, 15 }
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
                                            -20
                                            20
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
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -80 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                Pass: i16 = 4
                ColorLookUpTypeY: u8 = 3
                IsDirectionOriented: flag = true
                IsRandomStartFrame: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 22, 8, 0 }
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
                                    0.800000012
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 22, 8, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 2.496454, 0 }
                            { 0.5, 1.09219861, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_Embers.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.649999976
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 3
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.39999998
                }
                ParticleLinger: option[f32] = {
                    0.200000003
                }
                Lifetime: option[f32] = {
                    2.5
                }
                EmitterName: string = "firePillarADD"
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 5, 0, -80 }
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
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_R_Smoke_A.scb"
                    }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.56078434, 0.474509805, 0.333333343, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0201869775
                            0.728126705
                            1
                        }
                        Values: list[vec4] = {
                            { 0.56078434, 0.474509805, 0.333333343, 0 }
                            { 0.56078434, 0.474509805, 0.333333343, 1 }
                            { 0.56078434, 0.474509805, 0.333333343, 1 }
                            { 0.56078434, 0.474509805, 0.333333343, 0 }
                        }
                    }
                }
                Pass: i16 = 1
                AlphaRef: u8 = 0
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.150000006
                                0.725408375
                                0.78865701
                                0.930580735
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                                0.107954547
                                0.863636374
                                1
                            }
                        }
                    }
                    LingerErosionDriveCurve: embed = ValueFloat {
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
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_I_SmokeErode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                DisableBackfaceCull: bool = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 0, 0 }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.200000003, 0.349999994, 0.100000001 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.699999988
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
                                    0.699999988
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0.200000003, 0.349999994, 0.100000001 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.110590294
                            0.243071362
                            0.408427328
                            0.998387098
                        }
                        Values: list[vec3] = {
                            { 0.257142872, 0.5, 0.257142872 }
                            { 0.449579835, 0.7313025, 0.449579835 }
                            { 0.628571451, 0.88277334, 0.631311536 }
                            { 0.79285717, 1, 0.79285717 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_W_Cast_Beam.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 1.25 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 1 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0, 1 }
                        }
                    }
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_W_Cast_Beam.dds"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 1.5 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 80
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.20000005
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.504901946
                                    0.83006537
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.200000003
                                    0.394285709
                                    0.628571451
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
                    8
                }
                IsSingleParticle: flag = true
                EmitterName: string = "FlameStart1"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 400, 100 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 0, 0, 15 }
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
                                            -20
                                            20
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
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 80 }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.700007617 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00126742711
                            0.103393443
                            0.214542717
                            0.385573953
                            0.539355874
                            0.681520879
                            0.821419358
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 0.450980395, 0, 0.527064562 }
                            { 0.505882382, 0.321568638, 0, 0.700007617 }
                            { 0.274509817, 0.0274509806, 0, 0.700007617 }
                            { 0.286274523, 0, 0.20784314, 0.549025595 }
                            { 0.200000003, 0.00392156886, 0.235294119, 0.214119986 }
                            { 0.145098045, 0.192156866, 0.250980407, 0.0741184577 }
                            { 0.149019614, 0.149019614, 0.149019614, 0 }
                        }
                    }
                }
                Pass: i16 = -2
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 100
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
                    ErosionFeatherOut: f32 = 0.200000003
                    ErosionSliceWidth: f32 = 1.70000005
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_I_SmokeErode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 250, 0, 0 }
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
                            { 250, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 35, 35 }
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
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 100, 35, 35 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0648113042
                            0.176558331
                            0.517793298
                            0.990196049
                        }
                        Values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 0.830168068, 0.830168068, 0.830168068 }
                            { 1.19151783, 1.19151783, 1.19151783 }
                            { 1.53035712, 1.53035712, 1.53035712 }
                            { 1.85000002, 1.85000002, 1.85000002 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Morde_Skin03_Dust.dds"
                NumFrames: u16 = 8
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.649999976
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.200000003
                }
                ParticleLinger: option[f32] = {
                    10.1000004
                }
                Lifetime: option[f32] = {
                    1.03999996
                }
                IsSingleParticle: flag = true
                EmitterName: string = "LandFlash"
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 15, 80 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.275409698
                            0.855379164
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 0.850980401, 1 }
                            { 0.982758641, 0.982758641, 0.00392156886, 0.982758641 }
                            { 0.529411793, 0.0431372561, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 4
                AlphaRef: u8 = 0
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {}
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.150000006
                                0.343114376
                                0.482889682
                                1
                            }
                            Values: list[f32] = {
                                0
                                0.39049235
                                0.634380281
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.200000003
                    ErosionFeatherOut: f32 = 0.200000003
                    ErosionSliceWidth: f32 = 1.70000005
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_R_Ground_A_Errode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500999987
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    -0.600000024
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
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 60, 60, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 3.07236838, 3.07236838, 1 }
                            { 6, 6, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_Q_Flash.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 4, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.200000003
                }
                ParticleLinger: option[f32] = {
                    10.1000004
                }
                Lifetime: option[f32] = {
                    1.03999996
                }
                IsSingleParticle: flag = true
                EmitterName: string = "SpawnFlatFlash"
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 15, 80 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.247191012
                            0.611690402
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0, 1, 0.850980401, 1 }
                            { 0.686274529, 0.631372571, 0.00392156886, 0.819607854 }
                            { 0.529411793, 0.0431372561, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 4
                AlphaRef: u8 = 0
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {}
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.150000006
                                0.233678758
                                0.35846287
                                1
                            }
                            Values: list[f32] = {
                                0
                                0.54838711
                                0.858064532
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.200000003
                    ErosionFeatherOut: f32 = 0.200000003
                    ErosionSliceWidth: f32 = 1.70000005
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_R_Ground_A_Errode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500999987
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    -0.600000024
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
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 50, 50, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 6, 6, 1 }
                            { 3, 3, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_Q_Flash.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 4, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.649999976
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 10
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.300000012
                }
                Lifetime: option[f32] = {
                    8.5
                }
                EmitterName: string = "MainFlash1"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 80 }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.843137264, 0.474509805, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.652482271
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.333333343
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0.0178571437
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.489361703
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            0.018253969
                            0.0894522443
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 0.843137264, 0.474509805, 1 }
                            { 1, 0.843137264, 0.474509805, 0.648432076 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 3
                AlphaRef: u8 = 0
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 120
                }
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 90 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 90, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 320, 150, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 320, 150, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_Q_Flash.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.649999976
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 10
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.300000012
                }
                Lifetime: option[f32] = {
                    8.5
                }
                EmitterName: string = "MainFlash2"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 5, 80 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.843137264, 0.474509805, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.652482271
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.333333343
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0.0178571437
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.489361703
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            0.018253969
                            0.0894522443
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 0.843137264, 0.474509805, 1 }
                            { 1, 0.843137264, 0.474509805, 0.648432076 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 3
                AlphaRef: u8 = 0
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 320, 150, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 320, 150, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_Q_Flash.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Skin03/Particles/Mordekaiser_Skin03_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
            }
        }
        ParticleName: string = "Mordekaiser_Base_Passive_Dance_Fireworks"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Passive_Dance_Fireworks"
        mEyeCandy: bool = true
    }
}
