# IReusePool

IReusePool is a reuse pool interface for custom component.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getReusableInfo

```TypeScript
getReusableInfo(componentConstructor : Class, 
    reuseId?: string): IReusableInfo[] | IReusableInfo | undefined
```

Get IReusableInfo for given Component/V2 in the pool.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| componentConstructor | [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md) | Yes |
| reuseId | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IReusableInfo](arkts-arkui-utils-ireusableinfo-i.md)[] \| [IReusableInfo](arkts-arkui-utils-ireusableinfo-i.md) \| undefined |

## preRender

```TypeScript
preRender(builder: WrappedBuilder<CustomBuilder>, times: int): Promise<void>
```

The preRender function pre-render n instances and add to pool.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| builder | [WrappedBuilder](arkts-arkui-builder-wrappedbuilder-c.md)&lt;[CustomBuilder](arkts-arkui-custombuilder-t.md)&gt; | Yes |
| times | int | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
