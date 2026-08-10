# MonitorValueInfo

监听变量信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface MonitorValueInfo--><!--Device-unnamed-export declare interface MonitorValueInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## observeProps

```TypeScript
observeProps?: boolean
```

是否开启属性观察。

true：开启属性观察；false：不开启属性观察。

默认值：false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorValueInfo-observeProps?: boolean--><!--Device-MonitorValueInfo-observeProps?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path?: string
```

路径信息。未传入将使用自动生成的默认值。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorValueInfo-path?: string--><!--Device-MonitorValueInfo-path?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## valueCallback

```TypeScript
valueCallback: MonitorValueCallback
```

获取变量的回调。

**Type:** [MonitorValueCallback](arkts-arkui-monitorvaluecallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorValueInfo-valueCallback: MonitorValueCallback--><!--Device-MonitorValueInfo-valueCallback: MonitorValueCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

