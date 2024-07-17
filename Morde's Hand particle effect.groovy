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
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 1000 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.487096786
                            0.546774209
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 4.20168066 }
                            { 0, 0, 1000 }
                            { 0, 0, 1000 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { -50, -4, 80 }
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
                    ConstantValue: vec4 = { 0, 0.117647059, 0.0313725509, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.137592077
                            0.32766065
                            0.754119158
                            0.887198985
                            1
                        }
                        Values: list[vec4] = {
                            { 0, 0.117647059, 0.0313725509, 0 }
                            { 0, 0.116408668, 0.0310423113, 0.68387717 }
                            { 0, 0.117647059, 0.0313725509, 1 }
                            { 0, 0.117647059, 0.0313725509, 1 }
                            { 0, 0.0858131498, 0.0228835065, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                Pass: i16 = 400
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    ReflectionMapTexture: string = "ASSETS/Shared/Particles/Generic_White_Cubemap.SKINS_Lillia_Skin28.dds"
                    ReflectionOpacityDirect: f32 = 2
                    ReflectionOpacityGlancing: f32 = 2
                    ReflectionFresnelColor: vec4 = { 0, 0.211764708, 0.0980392173, 1 }
                    Fresnel: f32 = 0.0199999996
                    FresnelColor: vec4 = { 0, 0.211764708, 0.0980392173, 0 }
                }
                MiscRenderFlags: u8 = 1
                StencilMode: u8 = 2
                StencilRef: u8 = 2
                IsRotationEnabled: flag = true
                IsFollowingTerrain: flag = true
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -15, 0, 0 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 3, 0, 0 }
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