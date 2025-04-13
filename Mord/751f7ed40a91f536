#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_E_Spirit" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.150000006
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 4
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                EmitterName: string = "Glow"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 30, 0 }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 50, 60, 50 }
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
                                        -1
                                        1
                                    }
                                }
                            }
                            Times: list[f32] = {
                                0
                            }
                            Values: list[vec3] = {
                                { 50, 60, 50 }
                            }
                        }
                    }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    ScaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                    ScaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.223529428, 0.792156935, 1, 0.0980392247 }
                }
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
                Pass: i16 = 100
                AlphaRef: u8 = 0
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {}
                MiscRenderFlags: u8 = 1
                UvScrollClamp: flag = true
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 200, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 0 }
                            { 1, 1, 0 }
                            { 0.200000003, 1, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Illaoi/Skins/Base/Particles/Illaoi_Base_W_SoftAlpha.dds"
                TexAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = -1
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "MatOverride"
                BlendMode: u8 = 1
                Pass: i16 = 10000
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 0 }
                }
                Texture: string = "ASSETS/Characters/Illaoi/Skins/Base/Particles/Illaoi_Base_E_SpiritMat.dds"
                MaterialOverrideDefinitions: list[embed] = {
                    VfxMaterialOverrideDefinitionData {
                        BaseTexture: string = "ASSETS/Characters/Illaoi/Skins/Base/Particles/Illaoi_Base_E_SpiritMat.dds"
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.400000006
                }
                ParticleLinger: option[f32] = {
                    0.150000006
                }
                Lifetime: option[f32] = {
                    0.899999976
                }
                EmitterName: string = "DarkTrail"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 125 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 0.5 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 20, 0 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0829424337
                            0.33328107
                            0.740020931
                            0.877324998
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.862289011 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.353488386 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.00784313772, 0.321568638, 0.337254912, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0230549295
                            0.0717629418
                            0.164200529
                            0.271529645
                            0.585484803
                            1
                        }
                        Values: list[vec4] = {
                            { 0.00784313772, 0.321568638, 0.337254912, 0 }
                            { 0.00784313772, 0.321568638, 0.337254912, 0.708588541 }
                            { 0.00784313772, 0.321568638, 0.337254912, 1 }
                            { 0.00784313772, 0.321568638, 0.337254912, 1 }
                            { 0.00784313772, 0.321568638, 0.337254912, 0.866569459 }
                            { 0.00784313772, 0.321568638, 0.337254912, 0.380991727 }
                            { 0.00784313772, 0.321568638, 0.337254912, 0 }
                        }
                    }
                }
                Pass: i16 = 9
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                UseNavmeshMask: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 2, 2 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0796019882
                            0.140049756
                            0.390049756
                            0.75
                            1
                        }
                        Values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.400000006 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                            { 0.995205462, 0.995205462, 0.995205462 }
                            { 0.995205462, 0.995205462, 0.995205462 }
                            { 0.5, 0.5, 0.5 }
                            { 0.300000012, 0.300000012, 0.300000012 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Cast_Trail.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 200
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.200000003
                }
                ParticleLinger: option[f32] = {
                    0.150000006
                }
                Lifetime: option[f32] = {
                    0.25
                }
                EmitterName: string = "LightTrail"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 125 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 0.5 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 10, 0 }
                }
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0829424337
                            0.33328107
                            0.740020931
                            0.877324998
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.862289011 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.353488386 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 1, 0.635294139, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0431465916
                            0.123786286
                            0.289376348
                            0.59361124
                            0.810519934
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 1, 0.635294139, 0 }
                            { 0, 1, 0.635294139, 0.784313738 }
                            { 0, 1, 0.635294139, 1 }
                            { 0, 1, 0.635294139, 1 }
                            { 0, 1, 0.635294139, 0.833511591 }
                            { 0, 1, 0.635294139, 0.190909088 }
                            { 0, 1, 0.635294139, 0 }
                        }
                    }
                }
                Pass: i16 = 10
                AlphaRef: u8 = 0
                MiscRenderFlags: u8 = 1
                UseNavmeshMask: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 80, 2, 2 }
                }
                Scale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.800000012, 0.800000012, 0.800000012 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0796019882
                            0.140049756
                            0.390049756
                            0.75
                            1
                        }
                        Values: list[vec3] = {
                            { 0.319999993, 0.319999993, 0.319999993 }
                            { 0.720000029, 0.720000029, 0.720000029 }
                            { 0.796164393, 0.796164393, 0.796164393 }
                            { 0.796164393, 0.796164393, 0.796164393 }
                            { 0.400000006, 0.400000006, 0.400000006 }
                            { 0.239999995, 0.239999995, 0.239999995 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Cast_Trail.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.125
                }
                ParticleLinger: option[f32] = {
                    10.3999996
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "flash"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            0.25
                            0.75
                            1
                        }
                        Values: list[vec4] = {
                            { 0.149020001, 0.0784310028, 0.0784310028, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 0.988234997, 0.63529402, 1 }
                            { 0.223528996, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                Pass: i16 = 10
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
                    ConstantValue: vec3 = { 100, 100, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.25, 1.25, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/common_HitEffect.dds"
            }
        }
        ParticleName: string = "Mordekaiser_Base_E_Spirit"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_E_Spirit"
        Flags: u16 = 197
        BuildUpTime: f32 = 3
    }
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_E_aoe_Enemy" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.29999995
                }
                Lifetime: option[f32] = {
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Pit_Cap"
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 0, -43 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Pit_Cap_A.scb"
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0 }
                }
                Pass: i16 = -8
                MiscRenderFlags: u8 = 1
                StencilMode: u8 = 1
                StencilRef: u8 = 3
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.01999998, 1.01999998, 1.03999996 }
                }
                Texture: string = "ASSETS/Characters/Malzahar/Skins/Skin06/Particles/black.dds"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.300000012
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.699999988
                }
                Lifetime: option[f32] = {
                    1.60000002
                }
                IsSingleParticle: flag = true
                EmitterName: string = "newHandDarkAbove"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { -50, -20, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Hand_Inner.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Hand_RG.skl"
                        mAnimationName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell3_Hand.anm"
                    }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Lissandra/Skins/Base/Particles/common_color-eyefade32.dds"
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.117647059, 0.0235294122, 0, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.358064502
                            0.47096774
                            0.524780035
                            0.754119158
                            0.887198985
                            1
                        }
                        Values: list[vec4] = {
                            { 0.117647059, 0.0235294122, 0, 0 }
                            { 0.117647059, 0.0235294122, 0, 0.222126067 }
                            { 0.117647059, 0.0235294122, 0, 0.610192955 }
                            { 0.117647059, 0.0235294122, 0, 1 }
                            { 0.11570248, 0.0235294122, 0, 1 }
                            { 0.0858131498, 0.0171626303, 0, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 400
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    ReflectionMapTexture: string = "ASSETS/Shared/Particles/Generic_White_Cubemap.SKINS_Lillia_Skin28.dds"
                    ReflectionOpacityDirect: f32 = 2
                    ReflectionOpacityGlancing: f32 = 2
                    ReflectionFresnelColor: vec4 = { 1, 0.23137255, 0, 1 }
                    Fresnel: f32 = 0.0199999996
                    FresnelColor: vec4 = { 1, 0.250980407, 0, 0 }
                }
                StencilMode: u8 = 3
                StencilRef: u8 = 3
                IsRotationEnabled: flag = true
                IsFollowingTerrain: flag = true
                IsGroundLayer: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 500, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.0016129032
                            0.625806451
                            0.722580671
                            0.987096786
                        }
                        Values: list[vec3] = {
                            { 10.3626947, 0, 0 }
                            { 18.1347141, 0, 0 }
                            { 505.181335, 0, 0 }
                            { 492.227966, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 13, 13, 13 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.49032259
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/common_color-hold.dds"
                UvMode: u8 = 1
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, -0.25 }
                }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 2, 2 }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    1.79999995
                }
                IsSingleParticle: flag = true
                EmitterName: string = "CastCracksGlow"
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_B.scb"
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.011009085
                            0.651917458
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 11
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Ground_B_Glow.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Ground_B_Glow_Mult.dds"
                    TexAddressModeMult: u8 = 2
                    UvScrollClampMult: flag = true
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 1 }
                    }
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        ConstantValue: vec2 = { 0, 1 }
                        Dynamics: pointer = VfxAnimatedVector2fVariableData {
                            Times: list[f32] = {
                                0.00126742711
                                0.0633777827
                                0.223070383
                                0.42077294
                                1
                            }
                            Values: list[vec2] = {
                                { 0, -10 }
                                { 0, -7.85074663 }
                                { 0, -4.26258469 }
                                { 0, -2.35875702 }
                                { 0, 0 }
                            }
                        }
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    1.79999995
                }
                IsSingleParticle: flag = true
                EmitterName: string = "CastCracksGlow1"
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 2, -0.5, 0.100000001 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_B.scb"
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 0.13333334, 0.321568638, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.011009085
                            0.365131646
                            0.641241729
                            0.80281353
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 0.13333334, 0.321568638, 0 }
                            { 1, 0.13333334, 0.321568638, 1 }
                            { 1, 0.13333334, 0.321568638, 1 }
                            { 1, 0.13333334, 0.321568638, 0.809380531 }
                            { 1, 0.13333334, 0.321568638, 0 }
                        }
                    }
                }
                Pass: i16 = 14
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = -1.10000002
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0
                                0.0289623346
                                0.209761605
                                0.291349381
                                0.606664658
                                0.77271831
                            }
                            Values: list[f32] = {
                                -1.10000002
                                -1.10000002
                                -1.10000002
                                -0.94866997
                                -0
                                -0
                                -1.10000002
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.0500000007
                    ErosionFeatherOut: f32 = 0.0500000007
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_E_Slash_B_Erode.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.07000005, 1.07000005, 1.07000005 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Ground_B_Glow_Edge.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.100000001
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.400000006
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    1.20000005
                }
                IsSingleParticle: flag = true
                ChildParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    ChildrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            EffectKey: hash = "Mordekaiser_E_mis_Enemy"
                        }
                    }
                }
                EmitterName: string = "Shockwave"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -8000 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 9 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 120, 750 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Shockwave.scb"
                    }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.324624211
                            0.580138922
                            1
                        }
                        Values: list[vec4] = {
                            { 0.694117665, 0.694117665, 0.694117665, 0 }
                            { 1, 1, 0.996078432, 0 }
                            { 1, 0.990740716, 1, 0 }
                            { 0.4627451, 0.4627451, 0.4627451, 0 }
                        }
                    }
                }
                Pass: i16 = 12
                AlphaRef: u8 = 0
                DisableBackfaceCull: bool = true
                StencilMode: u8 = 1
                StencilRef: u8 = 2
                ParticleIsLocalOrientation: flag = true
                HasPostRotateOrientation: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 0.600000024, 1, 0.5 }
                            { 0.699999988, 0.5, 0.75 }
                            { 1, 0, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_Indicator_Mult.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.100000001, 0.100000001 }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.300000012
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.699999988
                }
                Lifetime: option[f32] = {
                    1.60000002
                }
                IsSingleParticle: flag = true
                EmitterName: string = "newHandDarkAbove2"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { -50, -20, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Hand_Inner.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Hand_RG.skl"
                        mAnimationName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell3_Hand.anm"
                    }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Lissandra/Skins/Base/Particles/common_color-eyefade32.dds"
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.117647059, 0.0235294122, 0, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.358064502
                            0.47096774
                            0.524780035
                            0.754119158
                            0.887198985
                            1
                        }
                        Values: list[vec4] = {
                            { 0.117647059, 0.0235294122, 0, 0 }
                            { 0.117647059, 0.0235294122, 0, 0.222126067 }
                            { 0.117647059, 0.0235294122, 0, 0.610192955 }
                            { 0.117647059, 0.0235294122, 0, 1 }
                            { 0.11570248, 0.0235294122, 0, 1 }
                            { 0.0858131498, 0.0171626303, 0, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 400
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    ReflectionMapTexture: string = "ASSETS/Shared/Particles/Generic_White_Cubemap.SKINS_Lillia_Skin28.dds"
                    ReflectionOpacityDirect: f32 = 2
                    ReflectionOpacityGlancing: f32 = 2
                    ReflectionFresnelColor: vec4 = { 1, 0.23137255, 0, 1 }
                    Fresnel: f32 = 0.0199999996
                    FresnelColor: vec4 = { 1, 0.250980407, 0, 0 }
                }
                MiscRenderFlags: u8 = 1
                StencilMode: u8 = 2
                StencilRef: u8 = 3
                IsRotationEnabled: flag = true
                IsFollowingTerrain: flag = true
                IsGroundLayer: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 500, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.0016129032
                            0.625806451
                            0.722580671
                            0.987096786
                        }
                        Values: list[vec3] = {
                            { 10.3626947, 0, 0 }
                            { 18.1347141, 0, 0 }
                            { 505.181335, 0, 0 }
                            { 492.227966, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 13, 13, 13 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.49032259
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/common_color-hold.dds"
                UvMode: u8 = 1
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, -0.25 }
                }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 2, 2 }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.300000012
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.39999998
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    1.79999995
                }
                IsSingleParticle: flag = true
                EmitterName: string = "SlashMarksAdd2"
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_A.scb"
                    }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.639993906 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.011009085
                            0.706152439
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.639993906 }
                            { 1, 1, 1, 0.639993906 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = -8
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_A.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_Wipe.dds"
                    TexAddressModeMult: u8 = 2
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 0.25 }
                    }
                    UvScrollClampMult: flag = true
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 0.800000012 }
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, -0.870000005 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.349999994
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.39999998
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    1.79999995
                }
                IsSingleParticle: flag = true
                EmitterName: string = "SlashMarksDark"
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_A_Dark.scb"
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.117647059, 0.0235294122, 0, 0.34117648 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.011009085
                            0.706152439
                            1
                        }
                        Values: list[vec4] = {
                            { 0.117647059, 0.0235294122, 0, 0.34117648 }
                            { 0.117647059, 0.0235294122, 0, 0.34117648 }
                            { 0.117647059, 0.0235294122, 0, 0 }
                        }
                    }
                }
                Pass: i16 = -9
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_A.dds"
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_Wipe.dds"
                    TexAddressModeMult: u8 = 2
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 0.25 }
                    }
                    UvScrollClampMult: flag = true
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 0.800000012 }
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, -0.870000005 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.180000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.850000024
                }
                Lifetime: option[f32] = {
                    0.300000012
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Pit_BG1"
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Pit_A.scb"
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.200000003, 0.200000003, 0.200000003, 0.380392164 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0516366959
                            0.483870953
                            0.943091094
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0.200000003, 0.200000003, 0.200000003, 0.380392164 }
                            { 0.200000003, 0.200000003, 0.200000003, 0.380392164 }
                            { 0.200000003, 0.200000003, 0.200000003, 0.380392164 }
                            { 0.200000003, 0.200000003, 0.200000003, 0 }
                        }
                    }
                }
                Pass: i16 = -7
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.0064516128
                                0.0417065546
                                0.166701347
                                0.347783566
                                0.628220618
                                0.713152945
                                0.883017719
                                1
                            }
                            Values: list[f32] = {
                                1
                                0.668393791
                                0.160621762
                                0
                                0
                                0.165803105
                                0.68911916
                                1
                            }
                        }
                    }
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_PitWipeIn.dds"
                }
                MiscRenderFlags: u8 = 1
                StencilMode: u8 = 2
                StencilRef: u8 = 3
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Ground_Spray_Mult.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 7, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 2, 1 }
                }
            }
        }
        VisibilityRadius: f32 = 2500
        ParticleName: string = "Mordekaiser_Base_E_aoe_Enemy"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_E_aoe_Enemy"
        SoundPersistentDefault: string = "Play_sfx_Mordekaiser_MordekaiserE_cast"
    }
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_E_Cast_Ground" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.100000001
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 65
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
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
                            0.800000012
                        }
                    }
                }
                Lifetime: option[f32] = {
                    0.699999988
                }
                EmitterName: string = "distortion"
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x6b77a8ca: embed = ValueColor {
                        Dynamics: pointer = VfxAnimatedColorVariableData {
                            Times: list[f32] = {
                                0
                                0.282331526
                                0.608378887
                                1
                            }
                            Values: list[vec4] = {
                                { 1, 1, 1, 1 }
                                { 1, 1, 1, 0.531661808 }
                                { 1, 1, 1, 0.205614477 }
                                { 1, 1, 1, 0 }
                            }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 1, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Ezreal/Skins/Skin05/Particles/common_alpha_20.dds"
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.102024756
                            0.314171463
                            0.419815063
                            0.530893028
                            0.642917871
                            0.866400659
                            0.978142083
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.00641025649 }
                            { 0.998353243, 0.998353243, 0.998353243, 0.16802007 }
                            { 0.994928956, 0.994928956, 0.994928956, 0.826923072 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.993589759, 0.993589759, 0.993589759, 0.848886251 }
                            { 0.993589759, 0.993589759, 0.993589759, 0.24517782 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = -1
                MeshRenderFlags: u8 = 0
                ColorLookUpScales: vec2 = { 0.699999988, 1 }
                ColorLookUpOffsets: vec2 = { 0.300000012, 0 }
                DistortionDefinition: pointer = VfxDistortionDefinitionData {
                    Distortion: f32 = 0.100000001
                    DistortionMode: u8 = 3
                    NormalMapTexture: string = "ASSETS/Characters/Ezreal/Skins/Skin05/Particles/common_distortion_soundwaves_01.dds"
                }
                StencilMode: u8 = 2
                StencilRef: u8 = 2
                IsUniformScale: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -90, 1, 0 }
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
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { -90, 1, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.0080461977
                            0.18413496
                            0.361013174
                            0.774110794
                            0.983443737
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.332319766, 0, 0 }
                            { 0.571252048, 0, 0 }
                            { 0.938232422, 0, 0 }
                            { 0.984375, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Ezreal/Skins/Skin05/Particles/common_Aura_Self_02.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLinger: option[f32] = {
                    10.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Reflection_Avatar3"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 10, 0 }
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {}
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.435294122, 0.435294122, 0.435294122, 1 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.149996191, 0.62999922, 0.379995435, 0.229999244 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00496688765
                            0.181419671
                            0.297025174
                            0.910357356
                            1
                        }
                        Values: list[vec4] = {
                            { 0.149996191, 0.62999922, 0.379995435, 0 }
                            { 0.149996191, 0.62999922, 0.379995435, 0 }
                            { 0.149996191, 0.62999922, 0.379995435, 0.229999244 }
                            { 0.149996191, 0.62999922, 0.379995435, 0.229999244 }
                            { 0.149996191, 0.62999922, 0.379995435, 0 }
                        }
                    }
                }
                Pass: i16 = 20
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    ReflectionOpacityDirect: f32 = 1
                    ReflectionOpacityGlancing: f32 = 0.0500000007
                    ReflectionFresnel: f32 = 0.0500000007
                    ReflectionFresnelColor: vec4 = { 0.0588235296, 0.800000012, 0.0823529437, 1 }
                }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                StencilMode: u8 = 2
                StencilRef: u8 = 2
                ParticleIsLocalOrientation: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 180, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, -1.20000005, 1 }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/common_color-hold.dds"
                UvMode: u8 = 1
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 0.200000003 }
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
            }
        }
        ParticleName: string = "Mordekaiser_Base_E_Cast_Ground"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_E_Cast_Ground"
    }
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_E_aoe_Ally" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.180000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.930000007
                }
                Lifetime: option[f32] = {
                    0.300000012
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Pit_BG"
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -20, 0 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Pit_A.scb"
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 0.39000535, 0.300007641, 0.200000003 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0516366959
                            0.943091094
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0, 0.39000535, 0.300007641, 0.200000003 }
                            { 0, 0.39000535, 0.300007641, 0.200000003 }
                            { 0, 0.39000535, 0.300007641, 0 }
                        }
                    }
                }
                Pass: i16 = -7
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.0064516128
                                0.0208740886
                                0.0740478635
                                0.112216443
                                0.628220618
                                1
                            }
                            Values: list[f32] = {
                                1
                                0.663212419
                                0.0932642519
                                0
                                0
                                1
                            }
                        }
                    }
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_PitWipeIn.dds"
                }
                MiscRenderFlags: u8 = 1
                StencilMode: u8 = 2
                StencilRef: u8 = 2
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Ground_Spray_Mult.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 2, 1 }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.5
                }
                Lifetime: option[f32] = {
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "mask_2"
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Pit_Cap_A.scb"
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0 }
                }
                Pass: i16 = -8
                MiscRenderFlags: u8 = 1
                StencilMode: u8 = 1
                StencilRef: u8 = 2
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Texture: string = "ASSETS/Characters/Malzahar/Skins/Skin06/Particles/black.dds"
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.180000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.930000007
                }
                Lifetime: option[f32] = {
                    0.300000012
                }
                IsSingleParticle: flag = true
                EmitterName: string = "soulBros"
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Pit_A.scb"
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.200000003 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.112903222
                            0.307666898
                            0.86043483
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0, 0, 0, 0 }
                            { 0.777070045, 0.783439517, 0.783439517, 0.1566879 }
                            { 1, 1, 1, 0.200000003 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = -6
                MiscRenderFlags: u8 = 1
                StencilMode: u8 = 2
                StencilRef: u8 = 2
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_E_Souls.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { -0.600000024, 0 }
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
                            { 1, 0 }
                        }
                    }
                }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 5, 1 }
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_PitWipe.dds"
                    TexAddressModeMult: u8 = 2
                    TexDivMult: vec2 = { 2, 1 }
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        ConstantValue: vec2 = { -2, 0 }
                        Dynamics: pointer = VfxAnimatedVector2fVariableData {
                            Times: list[f32] = {
                                0
                                0.49000001
                                0.5
                                1
                            }
                            Values: list[vec2] = {
                                { -0, 0 }
                                { -0, 0 }
                                { -2, 0 }
                                { -2, 0 }
                            }
                        }
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 0 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.180000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.930000007
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    0.300000012
                }
                IsSingleParticle: flag = true
                EmitterName: string = "pit_Edge3"
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Ledge.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.011009085
                            0.063808009
                            0.929903984
                            1
                        }
                        Values: list[vec4] = {
                            { 0.694117665, 0.694117665, 0.694117665, 0 }
                            { 1, 0.996078432, 0.996078432, 0.500007629 }
                            { 1, 0.990740716, 1, 0.500007629 }
                            { 0.4627451, 0.4627451, 0.4627451, 0 }
                        }
                    }
                }
                Pass: i16 = 2
                AlphaRef: u8 = 0
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.0064516128
                                0.0208740886
                                0.0740478635
                                0.112216443
                                0.628220618
                                1
                            }
                            Values: list[f32] = {
                                1
                                0.663212419
                                0.0932642519
                                0
                                0
                                1
                            }
                        }
                    }
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_PitWipeIn.dds"
                }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                StencilMode: u8 = 2
                StencilRef: u8 = 2
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_E_Ledge.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
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
                    ConstantValue: f32 = 0.5
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    1.79999995
                }
                IsSingleParticle: flag = true
                EmitterName: string = "CastCracksGlow"
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_B.scb"
                    }
                }
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.800000012 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.011009085
                            0.651917458
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.800000012 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 17
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                StencilMode: u8 = 2
                StencilRef: u8 = 2
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Ground_B_Glow.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Ground_B_Glow_Mult.dds"
                    TexAddressModeMult: u8 = 2
                    UvScrollClampMult: flag = true
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 1 }
                    }
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        ConstantValue: vec2 = { 0, 1 }
                        Dynamics: pointer = VfxAnimatedVector2fVariableData {
                            Times: list[f32] = {
                                0.00126742711
                                0.0633777827
                                0.223070383
                                0.42077294
                                1
                            }
                            Values: list[vec2] = {
                                { 0, -10 }
                                { 0, -7.85074663 }
                                { 0, -4.26258469 }
                                { 0, -2.35875702 }
                                { 0, 0 }
                            }
                        }
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.100000001
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.400000006
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    1.20000005
                }
                IsSingleParticle: flag = true
                ChildParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    ChildrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            EffectKey: hash = "Mordekaiser_E_mis"
                        }
                    }
                }
                EmitterName: string = "Shockwave"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -8000 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 9 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 120, 750 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Shockwave.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.800000012 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.011009085
                            0.324624211
                            0.580138922
                            1
                        }
                        Values: list[vec4] = {
                            { 0.694117665, 0.694117665, 0.694117665, 0 }
                            { 1, 1, 0.996078432, 0 }
                            { 1, 0.990740716, 1, 0 }
                            { 0.4627451, 0.4627451, 0.4627451, 0 }
                        }
                    }
                }
                Pass: i16 = 18
                AlphaRef: u8 = 0
                DisableBackfaceCull: bool = true
                StencilMode: u8 = 1
                StencilRef: u8 = 2
                ParticleIsLocalOrientation: flag = true
                HasPostRotateOrientation: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 0, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 0.600000024, 1, 0.5 }
                            { 0.699999988, 0.5, 0.75 }
                            { 1, 0, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_Indicator_Mult.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.100000001, 0.100000001 }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.75
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    1.20000005
                }
                IsSingleParticle: flag = true
                EmitterName: string = "rOCKWAVE"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -3000 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 0.5 }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 20, 1200 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Shockwave_C.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.800000012 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.13333334, 0.13333334, 0.13333334, 0.800000012 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.011009085
                            0.100252382
                            0.931111574
                            1
                        }
                        Values: list[vec4] = {
                            { 0.13333334, 0.13333334, 0.13333334, 0 }
                            { 0.13333334, 0.13333334, 0.132810459, 0.800000012 }
                            { 0.13333334, 0.132098764, 0.133292675, 0.800000012 }
                            { 0.13333334, 0.13333334, 0.13333334, 0 }
                        }
                    }
                }
                Pass: i16 = 8
                AlphaRef: u8 = 0
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/common_trans-vladnbladeback.dds"
                }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                StencilMode: u8 = 2
                StencilRef: u8 = 2
                ParticleIsLocalOrientation: flag = true
                HasPostRotateOrientation: flag = true
                IsRotationEnabled: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 0, 1 }
                            { 1, -0.600000024, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Ground_Spray.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 3 }
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Ground_Spray_Mult.dds"
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.300000012
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.699999988
                }
                Lifetime: option[f32] = {
                    1.60000002
                }
                IsSingleParticle: flag = true
                EmitterName: string = "newHandFresnel"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { -50, 5, 110 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Hand_Outer.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Hand_RG.skl"
                        mAnimationName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell3_Hand.anm"
                    }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Lissandra/Skins/Base/Particles/common_color-eyefade32.dds"
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 0, 0, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00633713556
                            0.563463569
                            0.86462146
                            0.984906554
                        }
                        Values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 402
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 120
                }
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    ReflectionMapTexture: string = "ASSETS/Shared/Particles/Generic_White_Cubemap.SKINS_Lillia_Skin28.dds"
                    ReflectionOpacityDirect: f32 = 2
                    ReflectionOpacityGlancing: f32 = 2
                    Fresnel: f32 = 0.00999999978
                    FresnelColor: vec4 = { 0.298039228, 1, 0.674509823, 0 }
                }
                IsRotationEnabled: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 13, 13, 13 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.49032259
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Lissandra/Skins/Base/Particles/common_color-hold.dds"
                UvMode: u8 = 1
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 2, 2 }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.300000012
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.699999988
                }
                Lifetime: option[f32] = {
                    1.60000002
                }
                IsSingleParticle: flag = true
                EmitterName: string = "newHandDarkAbove"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { -50, 0, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Hand_Inner.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Hand_RG.skl"
                        mAnimationName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell3_Hand.anm"
                    }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Lissandra/Skins/Base/Particles/common_color-eyefade32.dds"
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.800000012 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 0.0699931309, 0.0500038154, 0.800000012 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0909090936
                            0.754119158
                            0.887198985
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0.0699931309, 0.0500038154, 0 }
                            { 0, 0.0699931309, 0.0500038154, 0.800000012 }
                            { 0, 0.0699931309, 0.0500038154, 0.800000012 }
                            { 0, 0.0510538146, 0.0364733711, 0.800000012 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 400
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    ReflectionMapTexture: string = "ASSETS/Shared/Particles/Generic_White_Cubemap.SKINS_Lillia_Skin28.dds"
                    ReflectionOpacityDirect: f32 = 2
                    ReflectionOpacityGlancing: f32 = 2
                    ReflectionFresnelColor: vec4 = { 0, 0.149019614, 0.109803922, 1 }
                    Fresnel: f32 = 0.0199999996
                    FresnelColor: vec4 = { 0, 0.435294122, 0.325490206, 0 }
                }
                StencilMode: u8 = 3
                StencilRef: u8 = 2
                IsRotationEnabled: flag = true
                IsFollowingTerrain: flag = true
                IsGroundLayer: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 500, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.0016129032
                            0.625806451
                            0.722580671
                            0.987096786
                        }
                        Values: list[vec3] = {
                            { 10.3626947, 0, 0 }
                            { 18.1347141, 0, 0 }
                            { 505.181335, 0, 0 }
                            { 492.227966, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 13, 13, 13 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.49032259
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/common_color-hold.dds"
                UvMode: u8 = 1
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, -0.25 }
                }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 2, 2 }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.300000012
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.699999988
                }
                Lifetime: option[f32] = {
                    1.60000002
                }
                IsSingleParticle: flag = true
                EmitterName: string = "newHandDarkBelow"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { -50, 0, 100 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Hand_Inner.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Hand_RG.skl"
                        mAnimationName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Animations/Spell3_Hand.anm"
                    }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Lissandra/Skins/Base/Particles/common_color-eyefade32.dds"
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.800000012 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 0.0699931309, 0.0500038154, 0.800000012 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0909090936
                            0.754119158
                            0.887198985
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0.0699931309, 0.0500038154, 0 }
                            { 0, 0.0699931309, 0.0500038154, 0.800000012 }
                            { 0, 0.0699931309, 0.0500038154, 0.800000012 }
                            { 0, 0.0510538146, 0.0364733711, 0.800000012 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 400
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    ReflectionMapTexture: string = "ASSETS/Shared/Particles/Generic_White_Cubemap.SKINS_Lillia_Skin28.dds"
                    ReflectionOpacityDirect: f32 = 2
                    ReflectionOpacityGlancing: f32 = 2
                    ReflectionFresnelColor: vec4 = { 0, 0.149019614, 0.109803922, 1 }
                    Fresnel: f32 = 0.0199999996
                    FresnelColor: vec4 = { 0, 0.435294122, 0.325490206, 0 }
                }
                MiscRenderFlags: u8 = 5
                StencilMode: u8 = 2
                StencilRef: u8 = 2
                IsRotationEnabled: flag = true
                IsFollowingTerrain: flag = true
                IsGroundLayer: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 500, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.0016129032
                            0.625806451
                            0.722580671
                            0.987096786
                        }
                        Values: list[vec3] = {
                            { 10.3626947, 0, 0 }
                            { 18.1347141, 0, 0 }
                            { 505.181335, 0, 0 }
                            { 492.227966, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 13, 13, 13 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.49032259
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/common_color-hold.dds"
                UvMode: u8 = 1
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 12, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, -0.25 }
                }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 2, 2 }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.300000012
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.39999998
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    1.79999995
                }
                IsSingleParticle: flag = true
                EmitterName: string = "SlashMarksAdd"
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_A.scb"
                    }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.011009085
                            0.706152439
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = -8
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_A.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_Wipe.dds"
                    TexAddressModeMult: u8 = 2
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 0.25 }
                    }
                    UvScrollClampMult: flag = true
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 0.800000012 }
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, -0.870000005 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.300000012
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.39999998
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    1.79999995
                }
                IsSingleParticle: flag = true
                EmitterName: string = "SlashMarksDarkb"
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_A.scb"
                    }
                }
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0, 0.209994659, 0.2399939, 0.400000006 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.011009085
                            0.706152439
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0.209994659, 0.2399939, 0.400000006 }
                            { 0, 0.209994659, 0.2399939, 0.400000006 }
                            { 0, 0.209994659, 0.2399939, 0 }
                        }
                    }
                }
                Pass: i16 = -9
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_A.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_Slash_Wipe.dds"
                    TexAddressModeMult: u8 = 2
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 1, 0.25 }
                    }
                    UvScrollClampMult: flag = true
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 0.800000012 }
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, -0.870000005 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.180000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.930000007
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    0.300000012
                }
                IsSingleParticle: flag = true
                EmitterName: string = "pit_OverEdge"
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_OverLedge.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.800000012 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.011009085
                            0.063808009
                            0.929903984
                            1
                        }
                        Values: list[vec4] = {
                            { 0.694117665, 0.694117665, 0.694117665, 0 }
                            { 1, 0.996078432, 0.996078432, 0.800000012 }
                            { 1, 0.990740716, 1, 0.800000012 }
                            { 0.4627451, 0.4627451, 0.4627451, 0 }
                        }
                    }
                }
                Pass: i16 = 12
                AlphaRef: u8 = 0
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.0064516128
                                0.0897183865
                                0.203913242
                                0.325007915
                                0.628220618
                                1
                            }
                            Values: list[f32] = {
                                1
                                0.648060918
                                0.237203643
                                0
                                0
                                1
                            }
                        }
                    }
                    ErosionMapName: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_E_PitWipeIn.dds"
                }
                MiscRenderFlags: u8 = 1
                StencilRef: u8 = 2
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_E_Ledge.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
        }
        VisibilityRadius: f32 = 2500
        ParticleName: string = "Mordekaiser_Base_E_aoe_Ally"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_E_aoe_Ally"
        SoundPersistentDefault: string = "Play_sfx_Mordekaiser_MordekaiserE_cast"
    }
    "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Q_Hit" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
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
                EmitterName: string = "FlatFlash"
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        Dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.400000006 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.258452266
                            0.488774568
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.400000006 }
                            { 1, 1, 1, 0.400000006 }
                            { 1, 1, 1, 0.0925373137 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 4
                AlphaRef: u8 = 0
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {}
                IsUniformScale: flag = true
                IsRotationEnabled: flag = true
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
                            { 1, 0.5, 1 }
                            { 9, 8, 1 }
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
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.25
                }
                ParticleLinger: option[f32] = {
                    10.3000002
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "cameraFlash"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 150, 0 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0572072081
                            0.13738738
                            0.720720708
                            0.977477491
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0.143283576 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 0.988234997, 1, 0.800000012 }
                            { 1, 1, 1, 0.173134327 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 10
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
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
                    ConstantValue: vec3 = { 140, 140, 140 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.25, 1.25, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_Flash.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PalleteSrcMixColor: embed = ValueColor {
                        ConstantValue: vec4 = { 0.299992383, 0.590005338, 0.110002287, 0 }
                    }
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 5, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.300000012
                }
                ParticleLinger: option[f32] = {
                    10.3000002
                }
                Lifetime: option[f32] = {
                    0.200000003
                }
                IsSingleParticle: flag = true
                EmitterName: string = "under_color"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 10, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    ScaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                    ScaleEmitOffsetByBoundObjectSize: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00675675692
                            0.0402564742
                            0.5402565
                            0.997747719
                        }
                        Values: list[vec4] = {
                            { 1, 0.98975724, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0.970149279, 1, 0.479192644 }
                            { 1, 0.970149279, 0.970149279, 0 }
                        }
                    }
                }
                Pass: i16 = -1
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -90, 1, 0 }
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
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { -90, 1, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 200, 200, 200 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.25
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.600000024, 0.600000024, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Z_darkFuzz.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 4
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
                ParticleLinger: option[f32] = {
                    11
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "shards"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 1400, 100 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.347222209
                                    0.638888896
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.600000024
                                    0.637647033
                                    0.96941179
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 1400, 100 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 1, 1 }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -2400, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -2400, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    Flags: u8 = 1
                    Radius: f32 = 5
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 50, 0 }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.0299785864
                            0.0739819035
                            0.745741427
                            0.985010684
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.985074639, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 6
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                HasPostRotateOrientation: flag = true
                IsRandomStartFrame: flag = true
                IsRotationEnabled: flag = true
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
                            { 1, 0, 0 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 800, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.349999994
                                    0.649999976
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    -1
                                    1
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
                            { 800, 0, 0 }
                        }
                    }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.445396155
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 20, 50, 50 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    0.699999988
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.200000003
                                    0.25
                                    0.850000024
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
                            { 20, 50, 50 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        Values: list[vec3] = {
                            { 10, 0, 0 }
                            { 1, 0, 0 }
                            { 1, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_Embers.dds"
                NumFrames: u16 = 4
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 4, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0299999993
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.150000006
                }
                Lifetime: option[f32] = {
                    0.5
                }
                IsSingleParticle: flag = true
                EmitterName: string = "HitFlash"
                Primitive: pointer = VfxPrimitiveAttachedMesh {}
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00496688765
                            0.180665389
                            0.396839589
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.305970162 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 6
                DepthBiasFactors: vec2 = { 0, 2 }
                MiscRenderFlags: u8 = 1
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 20, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.150000006
                            0.379032254
                            1
                        }
                        Values: list[vec3] = {
                            { 20, 0, 0 }
                            { 7.77070045, 0, 0 }
                            { 3.43949056, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/common_color-hold.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Mordekaiser/Skins/Base/Particles/Mordekaiser_Base_colorGrad_16.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 4, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
                EmitterUvScrollRate: vec2 = { 0, -1 }
            }
        }
        ParticleName: string = "Mordekaiser_Base_Q_Hit"
        ParticlePath: string = "Characters/Mordekaiser/Skins/Skin0/Particles/Mordekaiser_Base_Q_Hit"
        Flags: u16 = 198
    }
}
