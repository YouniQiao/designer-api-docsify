# EnvPropsOptions

Defining the EnvPropsOptions interface

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface EnvPropsOptions--><!--Device-unnamed-export declare interface EnvPropsOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultValue

```TypeScript
defaultValue: int | long | double | string | boolean
```

查询不到环境变量key，则使用defaultValue作为默认值存入AppStorage中。

**Type:** int \| long \| double \| string \| boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EnvPropsOptions-defaultValue: int | long | double | string | boolean--><!--Device-EnvPropsOptions-defaultValue: int | long | double | string | boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key: string
```

环境变量名称，支持的范围详见内置环境变量说明。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EnvPropsOptions-key: string--><!--Device-EnvPropsOptions-key: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

