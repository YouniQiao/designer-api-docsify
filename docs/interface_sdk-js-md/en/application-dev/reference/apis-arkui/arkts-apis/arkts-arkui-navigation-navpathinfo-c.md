# NavPathInfo

Indicates the information of NavDestination.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(name: string, param: Object | null | undefined, onPop?: Callback<PopInfo>, isEntry?: boolean)
```

Creates an instance of NavPathInfo.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [name](#name) | string | Yes |
| [param](#param) | Object \| null \| undefined | Yes |
| [onPop](#onpop) | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PopInfo](arkts-arkui-navigation-popinfo-i.md)&gt; | No |
| [isEntry](#isentry) | boolean | No |

## isEntry

```TypeScript
set isEntry(isEntry: boolean | undefined)
```

Set whether it is an entry destination, the default value is false, undefined means set to default value.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
set name(name: string)
```

Set the name of NavDestination.

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navDestinationId

```TypeScript
get navDestinationId(): string | undefined
```

The unique id of NavDestination.

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPop

```TypeScript
set onPop(onPop: Callback<PopInfo> | undefined)
```

Set the callback when next page returns, the default value is nullptr, undefined means set to default value.

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PopInfo](arkts-arkui-navigation-popinfo-i.md)&gt;

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## param

```TypeScript
set param(param: Object | null | undefined)
```

Set the detailed parameter of the NavDestination, default value is undefined, null is also a meaningful input parameter.

**Type:** Object

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
