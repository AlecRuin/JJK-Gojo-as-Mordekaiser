#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_R_Spirit_HeartBeat" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.200000003
                }
                Lifetime: option[f32] = {
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Heartbeat_A"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
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
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 80, 100, 100 }
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
                TimeBeforeFirstEmission: f32 = 0.25
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1.79999995
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.200000003
                }
                Lifetime: option[f32] = {
                    0.5
                }
                EmitterName: string = "Heartbeat_B"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
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
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 30, 50, 50 }
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
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 6
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
                                    0.200000003
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
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "EMBERS"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 400, 100, 400 }
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
                            { 400, 100, 400 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 3, 5 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 10, 10, 0 }
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
                                { 10, 10, 0 }
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
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Veigar/Skins/Base/Particles/common_color-smoke32_07.dds"
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.0202702694
                            0.0396375023
                            0.997747719
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.987878799, 0.987878799, 0.987878799, 0.987878799 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 1
                MeshRenderFlags: u8 = 0
                ColorRenderFlags: u8 = 1
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
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
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 6, 6, 6 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0759999976
                            0.869799674
                            1
                        }
                        Values: list[vec3] = {
                            { 10, 10, 10 }
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
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                Lifetime: option[f32] = {
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "darkHeartBak1"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Flags: u8 = 1
                }
                ParticleColorTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_alpha_02.dds"
                BlendMode: u8 = 2
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.352941185, 0.600000024, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.113025881
                            0.97499907
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.352941185, 0.600000024, 1 }
                            { 1, 0.352941185, 0.600000024, 1 }
                            { 1, 0.352941185, 0.600000024, 1 }
                            { 1, 0.352941185, 0.600000024, 1 }
                        }
                    }
                }
                Pass: i16 = 19
                MeshRenderFlags: u8 = 0
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 120, 1, 1 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Z_SoftSphere.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 6
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
                                    0.200000003
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
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "EMBERS1"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 400, 100, 400 }
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
                            { 400, 100, 400 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 3, 5 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 10, 10, 0 }
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
                                { 10, 10, 0 }
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
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Veigar/Skins/Base/Particles/common_color-smoke32_07.dds"
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.0202702694
                            0.0396375023
                            0.997747719
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.987878799, 0.987878799, 0.987878799, 0.987878799 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Pass: i16 = 1
                MeshRenderFlags: u8 = 0
                ColorRenderFlags: u8 = 1
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
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
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 6, 6, 6 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0759999976
                            0.869799674
                            1
                        }
                        Values: list[vec3] = {
                            { 10, 10, 10 }
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
        }
        ParticleName: string = "Mordekaiser_Base_R_Spirit_HeartBeat"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_R_Spirit_HeartBeat"
        Flags: u16 = 132
    }
}
