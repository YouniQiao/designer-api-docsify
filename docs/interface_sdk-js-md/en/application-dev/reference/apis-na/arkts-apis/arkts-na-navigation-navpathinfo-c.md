# NavPathInfo

Indicates the information of NavDestination.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class NavPathInfo--><!--Device-unnamed-export declare class NavPathInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(name: string, param: Object | null | undefined, onPop?: Callback<PopInfo>, isEntry?: boolean)
```

Creates an instance of NavPathInfo.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-constructor(name: string, param: Object | null | undefined, onPop?: Callback<PopInfo>, isEntry?: boolean)--><!--Device-NavPathInfo-constructor(name: string, param: Object | null | undefined, onPop?: Callback<PopInfo>, isEntry?: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of NavDestination. |
| param | Object \| null \| undefined | Yes | The detailed parameter of the NavDestination. |
| onPop | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[PopInfo](arkts-na-navigation-popinfo-i.md)&gt; | No | The callback when next page returns. |
| isEntry | boolean | No | Indicates whether it is an entry destination. |

