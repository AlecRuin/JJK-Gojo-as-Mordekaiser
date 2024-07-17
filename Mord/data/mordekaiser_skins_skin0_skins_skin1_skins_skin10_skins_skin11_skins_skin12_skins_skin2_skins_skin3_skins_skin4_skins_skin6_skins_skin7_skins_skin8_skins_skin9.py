#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Passive_Hit_Linger_Enemy" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 100
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.400000006
                }
                ParticleLinger: option[f32] = {
                    0.100000001
                }
                EmitterName: string = "DarkTrailFlat"
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 800, 0, 800 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 800, 0, -400 }
                            { 800, 0, 400 }
                            { 400, 0, 800 }
                        }
                    }
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
                                { 1, 1, 1, 0 }
                            }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { -50, 80, 0 }
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
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.564705908, 0.564705908, 0.564705908, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.123266563
                            0.320477366
                            0.403351039
                            0.450853437
                            0.508158267
                            0.613144219
                            0.775418282
                            1
                        }
                        Values: list[vec4] = {
                            { 0.564705908, 0.564705908, 0.564705908, 0 }
                            { 0.564705908, 0.564705908, 0.564705908, 0.206585169 }
                            { 0.564705908, 0.564705908, 0.564705908, 0.851126373 }
                            { 0.564705908, 0.564705908, 0.564705908, 1 }
                            { 0.564705908, 0.564705908, 0.564705908, 1 }
                            { 0.564705908, 0.564705908, 0.564705908, 0.948927581 }
                            { 0.564705908, 0.564705908, 0.564705908, 0.60784018 }
                            { 0.564705908, 0.564705908, 0.564705908, 0.189391032 }
                            { 0.564705908, 0.564705908, 0.564705908, 0 }
                        }
                    }
                }
                Pass: i16 = 10
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 70, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 220, 2, 2 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Cast_Trail.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16_purple.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                }
                EmitterUvScrollRate: vec2 = { -0.800000012, 0 }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Cast_Trail.dds"
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        ConstantValue: vec2 = { 0.5, 0 }
                        Dynamics: pointer = VfxAnimatedVector2fVariableData {
                            Times: list[f32] = {
                                0
                            }
                            Values: list[vec2] = {
                                { 0.5, 0 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 100
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.300000012
                }
                ParticleLinger: option[f32] = {
                    0.100000001
                }
                EmitterName: string = "LightTrailFlat"
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 800, 0, 800 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 800, 0, -400 }
                            { 800, 0, 400 }
                            { 400, 0, 800 }
                        }
                    }
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
                                { 1, 1, 1, 0 }
                            }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { -50, 80, 0 }
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
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.123266563
                            0.320477366
                            0.403351039
                            0.450853437
                            0.508158267
                            0.613144219
                            0.775418282
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.103294164 }
                            { 1, 1, 1, 0.425569683 }
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0.474471033 }
                            { 1, 1, 1, 0.303924739 }
                            { 1, 1, 1, 0.0946969613 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 11
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 70, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 150, 2, 2 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Cast_Trail.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16_purple.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                }
                EmitterUvScrollRate: vec2 = { -1.20000005, 0 }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Cast_Trail.dds"
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        ConstantValue: vec2 = { 0.5, 0 }
                        Dynamics: pointer = VfxAnimatedVector2fVariableData {
                            Times: list[f32] = {
                                0
                            }
                            Values: list[vec2] = {
                                { 0.5, 0 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 10
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.600000024
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
                            0.600000024
                        }
                    }
                }
                EmitterName: string = "soulFlakes"
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 800, 0, 800 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 800, 0, 0 }
                            { 0, 0, 800 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 0, 200, 0 }
                        Dynamics: pointer = VfxAnimatedVector3fVariableData {
                            ProbabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                                VfxProbabilityTableData {}
                            }
                            Times: list[f32] = {
                                0
                            }
                            Values: list[vec3] = {
                                { 0, 200, 0 }
                            }
                        }
                    }
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
                Rotation0: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 16, 16, 16 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 16, 16, 16 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 15, 15, 15 }
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
                            { 1, 1, 1 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Embers.dds"
                NumFrames: u16 = 3
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16_purple.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                TexDiv: vec2 = { 2, 2 }
            }
        }
        ParticleName: string = "Mordekaiser_Base_Passive_Hit_Linger_Enemy"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Passive_Hit_Linger_Enemy"
    }
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Passive_Hit_Streak_Enemy" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 20
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.100000001
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                    3
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.100000001
                        }
                    }
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "ImpactSharpSparks"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 900, 0, 700 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 7, 7, 7 }
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
                                            20
                                            -20
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
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.110573724
                            0.2850658
                            0.644805551
                            0.979166687
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.509803951 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.242718443 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 13
                MiscRenderFlags: u8 = 1
                IsDirectionOriented: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 25, 80, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
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
                            { 25, 80, 0 }
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
                            { 0.5, 0.400000006, 1 }
                            { 1, 2, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_Flash.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16_purple.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 10
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.449999988
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.440322578
                                    0.564516127
                                    0.693548381
                                    0.909677446
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    0.143533215
                                    0.316953242
                                    0.709309936
                                    0.96663475
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.449999988
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    3
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
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
                EmitterName: string = "darkEmbers"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 700, 400, 500 }
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
                                    0.100000001
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 700, 400, 500 }
                        }
                    }
                }
                Drag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2, 0.5, 0.5 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                            { 2, 0.5, 0.5 }
                        }
                    }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -2000, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -2000, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    Flags: u8 = 1
                    Size: vec3 = { 20, 20, 40 }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { -10, 0, -10 }
                }
                BlendMode: u8 = 2
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec4] = {
                            { 0.435294122, 0, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                MeshRenderFlags: u8 = 0
                DisableBackfaceCull: bool = true
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
                            0.0462962948
                            0.111111112
                            0.251241505
                            0.869799674
                            1
                        }
                        Values: list[vec3] = {
                            { 0.50444597, 0.50444597, 0.50444597 }
                            { 7.15493965, 7.2072506, 7.2072506 }
                            { 8.47820473, 8.28346252, 8.28346252 }
                            { 1.98611426, 1.98611426, 1.98611426 }
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
                ParticleLinger: option[f32] = {
                    10.1999998
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "darkflash"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 300, 0, 190 }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 10, 0, 0 }
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
                    ConstantValue: vec4 = { 0.70588237, 1, 0.968627453, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0539906099
                            0.154929578
                            0.535211265
                            1
                        }
                        Values: list[vec4] = {
                            { 0.823529422, 0.70588237, 1, 1 }
                            { 0.823529422, 0.70588237, 1, 1 }
                            { 0.823529422, 0.70588237, 1, 0.47984457 }
                            { 0.823529422, 0.70588237, 1, 0.0995628834 }
                            { 0.823529422, 0.70588237, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 7
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 300, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.44860065
                            0.713680744
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.881317079, 0.881317079, 0.881317079 }
                            { 0.617521763, 0.634124875, 0.634124875 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_Flash.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.300000012
                }
                ParticleLinger: option[f32] = {
                    10.1999998
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "lightFlash"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 350, 0, 220 }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { -10, 0, 0 }
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
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.620004594 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.126644731
                            0.333881587
                            0.535211265
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.620004594 }
                            { 1, 1, 1, 0.620004594 }
                            { 1, 1, 1, 0.297505826 }
                            { 1, 1, 1, 0.0617294423 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 12
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
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
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 160, 80, 80 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    5
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
                            { 160, 80, 80 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0406376868
                            0.221236303
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.947504163, 0.947504163, 0.947504163 }
                            { 0.66356492, 0.680168033, 0.680168033 }
                            { 0.200000003, 0.200000003, 0.200000003 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_Flash.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16_purple.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
        }
        ParticleName: string = "Mordekaiser_Base_Passive_Hit_Streak_Enemy"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Passive_Hit_Streak_Enemy"
    }
}
