# SuppressWarningsType

支持消除告警的规则。帮助开发者根据实际需求选择性地屏蔽兼容性告警、多设备告警、权限告警等，在确保代码质量的同时减少不必要的告警干扰，提升开发体验。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-export const enum SuppressWarningsType--><!--Device-unnamed-export const enum SuppressWarningsType-End-->

**System capability:** SystemCapability.Base

## COMPATIBILITY

```TypeScript
COMPATIBILITY = 'compatibility'
```

支持消除兼容性告警。当调用API的起始版本高于工程设置的兼容SDK版本时（build-profile.json5中指定的compatibleSdkVersion）产生的告警。建议在已做版本判断或兼容性处理时使用，避免盲目抑制告警导致低版本设备运行异常。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-SuppressWarningsType-COMPATIBILITY = 'compatibility'--><!--Device-SuppressWarningsType-COMPATIBILITY = 'compatibility'-End-->

**System capability:** SystemCapability.Base

## SYSCAP

```TypeScript
SYSCAP = 'syscap'
```

支持消除多设备告警。当调用API的系统能力在目标设备上不支持时产生的告警。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-SuppressWarningsType-SYSCAP = 'syscap'--><!--Device-SuppressWarningsType-SYSCAP = 'syscap'-End-->

**System capability:** SystemCapability.Base

## PERMISSION

```TypeScript
PERMISSION = 'permission'
```

支持消除权限告警。当调用需要权限的API但未在配置文件中声明相应权限时产生的告警。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-SuppressWarningsType-PERMISSION = 'permission'--><!--Device-SuppressWarningsType-PERMISSION = 'permission'-End-->

**System capability:** SystemCapability.Base

