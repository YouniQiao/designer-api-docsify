# NavPathInfo

Indicates the information of NavDestination.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class NavPathInfo--><!--Device-unnamed-export declare class NavPathInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(name: string, param: Object | null | undefined, onPop?: Callback<PopInfo>, isEntry?: boolean)
```

Creates an instance of NavPathInfo.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-constructor(name: string, param: Object | null | undefined, onPop?: Callback<PopInfo>, isEntry?: boolean)--><!--Device-NavPathInfo-constructor(name: string, param: Object | null | undefined, onPop?: Callback<PopInfo>, isEntry?: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of NavDestination. |
| param | Object \| null \| undefined | Yes | The detailed parameter of the NavDestination. |
| onPop | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;PopInfo&gt; | No | The callback when next page returns. |
| isEntry | boolean | No | Indicates whether it is an entry destination. |

## isEntry

```TypeScript
set isEntry(isEntry: boolean | undefined)
```

Set whether it is an entry destination, the default value is false, undefined means set to default value.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-set isEntry(isEntry: boolean | undefined)--><!--Device-NavPathInfo-set isEntry(isEntry: boolean | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
set name(name: string)
```

Set the name of NavDestination.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-set name(name: string)--><!--Device-NavPathInfo-set name(name: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navDestinationId

```TypeScript
get navDestinationId(): string | undefined
```

The unique id of NavDestination.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-get navDestinationId(): string | undefined--><!--Device-NavPathInfo-get navDestinationId(): string | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPop

```TypeScript
set onPop(onPop: Callback<PopInfo> | undefined)
```

Set the callback when next page returns, the default value is nullptr, undefined means set to default value.

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;PopInfo&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-set onPop(onPop: Callback<PopInfo> | undefined)--><!--Device-NavPathInfo-set onPop(onPop: Callback<PopInfo> | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## param

```TypeScript
set param(param: Object | null | undefined)
```

Set the detailed parameter of the NavDestination, default value is undefined,null is also a meaningful input parameter.

**Type:** Object

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-set param(param: Object | null | undefined)--><!--Device-NavPathInfo-set param(param: Object | null | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

