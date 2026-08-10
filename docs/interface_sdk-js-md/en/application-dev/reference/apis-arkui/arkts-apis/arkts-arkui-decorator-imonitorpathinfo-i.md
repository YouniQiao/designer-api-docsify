# IMonitorPathInfo

Defines Monitor path with its accessor interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IMonitorPathInfo--><!--Device-unnamed-export declare interface IMonitorPathInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## valueCallback

```TypeScript
valueCallback: MonitorValueCallback
```

Callback function to access monitored value.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMonitorPathInfo-valueCallback: MonitorValueCallback--><!--Device-IMonitorPathInfo-valueCallback: MonitorValueCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableWildcard

```TypeScript
enableWildcard?: boolean
```

启用通配符功能。设置为true可启用通配符功能，设置为false可禁用通配符功能。默认值为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMonitorPathInfo-enableWildcard?: boolean--><!--Device-IMonitorPathInfo-enableWildcard?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path: string
```

Changed paths(keys)

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMonitorPathInfo-path: string--><!--Device-IMonitorPathInfo-path: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

