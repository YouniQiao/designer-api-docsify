# MacroQuery

MacroQuery provides the API to check the support for macro photography.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface MacroQuery--><!--Device-camera-interface MacroQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## isMacroSupported

```TypeScript
isMacroSupported(): boolean
```

Checks whether macro photography is supported in the current state. This API must be called after  
[commitConfig]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MacroQuery-isMacroSupported(): boolean--><!--Device-MacroQuery-isMacroSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for the support of macro photography. **true** if supported, **false** otherwise. |

