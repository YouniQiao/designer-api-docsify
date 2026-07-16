# ParticleColorPropertyUpdaterConfigs

Defines the particle color property updater configs.

**Since:** 10

<!--Device-unnamed-interface ParticleColorPropertyUpdaterConfigs--><!--Device-unnamed-interface ParticleColorPropertyUpdaterConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [ParticleUpdater.CURVE]

```TypeScript
[ParticleUpdater.CURVE]: Array<ParticlePropertyAnimation<ResourceColor>>
```

The color changes with the animation curve. The array type indicates that multiple animation segments can be set for the current property, for example, 0–3000 ms, 3000–5000 ms, and 5000–8000 ms.

**Type:** Array<ParticlePropertyAnimation<ResourceColor>>

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticleColorPropertyUpdaterConfigs-[ParticleUpdater.CURVE]: Array<ParticlePropertyAnimation<ResourceColor>>--><!--Device-ParticleColorPropertyUpdaterConfigs-[ParticleUpdater.CURVE]: Array<ParticlePropertyAnimation<ResourceColor>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [ParticleUpdater.NONE]

```TypeScript
[ParticleUpdater.NONE]: void
```

The color does not change.

**Type:** void

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticleColorPropertyUpdaterConfigs-[ParticleUpdater.NONE]: void--><!--Device-ParticleColorPropertyUpdaterConfigs-[ParticleUpdater.NONE]: void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [ParticleUpdater.RANDOM]

```TypeScript
[ParticleUpdater.RANDOM]: ParticleColorOptions
```

The color changes randomly, with the per-second change difference being a value randomly generated from the range.The target color is obtained by applying the change difference to the current color value of each of the R, G, B, A channels.

**Type:** ParticleColorOptions

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticleColorPropertyUpdaterConfigs-[ParticleUpdater.RANDOM]: ParticleColorOptions--><!--Device-ParticleColorPropertyUpdaterConfigs-[ParticleUpdater.RANDOM]: ParticleColorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

