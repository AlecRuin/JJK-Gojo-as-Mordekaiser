#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Passive_Hit" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
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
                ChildParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    ChildrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            EffectKey: hash = "Mordekaiser_Passive_Hit_Streak"
                        }
                    }
                }
                EmitterName: string = "flash"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 0, 0 }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    Flags: u8 = 1
                    Size: vec3 = { 0, 50, 20 }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { -20, 100, 0 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0539906099
                            0.154929578
                            0.535211265
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.47984457 }
                            { 1, 1, 1, 0.0995628834 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 17
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 80, 80, 1 }
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
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/common_Black.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 1, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
        }
        ParticleName: string = "Mordekaiser_Base_Passive_Hit"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Passive_Hit"
        Flags: u16 = 132
    }
}
