# ParticleUpdaterOptions

Defines the particle updater options. > **NOTE** > > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-interface ParticleUpdaterOptions<TYPE, UPDATER extends ParticleUpdater>--><!--Device-unnamed-interface ParticleUpdaterOptions<TYPE, UPDATER extends ParticleUpdater>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## config

```TypeScript
config: ParticlePropertyUpdaterConfigs<TYPE>[UPDATER]
```

How the property is updated. The available options of **type** are as follows: 1. **ParticleUpdater.NONE**: The property does not change. In this case, the **config** type is [ParticlePropertyUpdaterConfigs]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_[ParticleUpdater.NONE]. 2. **ParticleUpdater.RANDOM**: The property changes randomly. In this case, the **config** type is [ParticlePropertyUpdaterConfigs]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_[ParticleUpdater.RANDOM]. 3. **ParticleUpdater.CURVE**: The property changes with the animation curve. In this case, the **config** type is [ParticlePropertyUpdaterConfigs]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_[ParticleUpdater.CURVE].

**Type:** ParticlePropertyUpdaterConfigs&lt;TYPE&gt;[UPDATER]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticleUpdaterOptions-config: ParticlePropertyUpdaterConfigs<TYPE>[UPDATER]--><!--Device-ParticleUpdaterOptions-config: ParticlePropertyUpdaterConfigs<TYPE>[UPDATER]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: UPDATER
```

Particle updater type.

**Type:** UPDATER

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticleUpdaterOptions-type: UPDATER--><!--Device-ParticleUpdaterOptions-type: UPDATER-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

