# EnvPropsOptions

用于指定环境变量名称及其默认值的键值对对象，作为[envProps](arkts-arkui-environment-c.md#envprops)参数传入。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface EnvPropsOptions--><!--Device-unnamed-declare interface EnvPropsOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultValue

```TypeScript
defaultValue: number | string | boolean
```

查询不到环境变量key，则使用defaultValue作为默认值存入AppStorage中。

**Type:** number \| string \| boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EnvPropsOptions-defaultValue: number | string | boolean--><!--Device-EnvPropsOptions-defaultValue: number | string | boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key: string
```

环境变量名称，支持的范围详见[内置环境变量说明](arkts-arkui-environment-c.md)。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EnvPropsOptions-key: string--><!--Device-EnvPropsOptions-key: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

