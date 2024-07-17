#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Mace_Idle" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {}
        ParticleName: string = "Mordekaiser_Base_Mace_Idle"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Mace_Idle"
    }
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_I_Glow" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 4
                }
                EmitterName: string = "bodyGlow"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xc1abfc9e
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = -260
                MeshRenderFlags: u8 = 0
                DepthBiasFactors: vec2 = { -1, -2 }
                DisableBackfaceCull: bool = true
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Mask_Glow.dds"
                UvMode: u8 = 2
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/mordekaiser_base_colorgrad_16_desat.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 4, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.0500000007, 0.0500000007 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -2
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    2
                                    -2
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0.0500000007, 0.0500000007 }
                        }
                    }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        Values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_CausticShade_Add.dds"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 4, 4 }
                    }
                    UvScrollAlphaMult: flag = false
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 0.125 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = -1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "softGloFront"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 30, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_alpha_02.dds"
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.659998477 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.270588249 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.165108964
                            0.799192607
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.270588249 }
                            { 1, 1, 1, 0.270588249 }
                            { 1, 1, 1, 0.270588249 }
                            { 1, 1, 1, 0.270588249 }
                        }
                    }
                }
                Pass: i16 = -259
                MeshRenderFlags: u8 = 0
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 130, 1, 1 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Z_SoftSphere.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16_desat.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 4, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
        }
        ParticleName: string = "Mordekaiser_Base_I_Glow"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_I_Glow"
    }
}
