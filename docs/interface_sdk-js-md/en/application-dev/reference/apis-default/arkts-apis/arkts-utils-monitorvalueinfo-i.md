# MonitorValueInfo

Define MonitorValueInfo.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface MonitorValueInfo--><!--Device-unnamed-export declare interface MonitorValueInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## observeProps

```TypeScript
observeProps?: boolean
```

Enable property observation. Set to true to enable property observation, and set to false to disable it. Default value is false.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorValueInfo-observeProps?: boolean--><!--Device-MonitorValueInfo-observeProps?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path?: string
```

Override path.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorValueInfo-path?: string--><!--Device-MonitorValueInfo-path?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## valueCallback

```TypeScript
valueCallback: MonitorValueCallback
```

the function triggered when state variable changes.

**Type:** [MonitorValueCallback](arkts-monitorvaluecallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorValueInfo-valueCallback: MonitorValueCallback--><!--Device-MonitorValueInfo-valueCallback: MonitorValueCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

