# StartupConfig

The module defines the configuration of \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export default interface StartupConfig--><!--Device-unnamed-export default interface StartupConfig-End-->

**System capability:** SystemCapability.Ability.AppStartup

## startupListener

```TypeScript
startupListener?: StartupListener
```

AppStartup listener, which is called when all the startup tasks are complete.

**Type:** StartupListener

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupConfig-startupListener?: StartupListener--><!--Device-StartupConfig-startupListener?: StartupListener-End-->

**System capability:** SystemCapability.Ability.AppStartup

## timeoutMs

```TypeScript
timeoutMs?: int
```

Timeout for executing all startup tasks, measured in ms. The default value is 10000 ms.

**Type:** int

**Default:** 10000

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupConfig-timeoutMs?: int--><!--Device-StartupConfig-timeoutMs?: int-End-->

**System capability:** SystemCapability.Ability.AppStartup

