# IReusePool

IReusePool is a reuse pool interface for custom component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export declare interface IReusePool--><!--Device-unnamed-export declare interface IReusePool-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getReusableInfo

```TypeScript
getReusableInfo(componentConstructor : Class, 
    reuseId?: string): IReusableInfo[] | IReusableInfo | undefined
```

Get IReusableInfo for given Component/V2 in the pool.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IReusePool-getReusableInfo(componentConstructor : Class,     reuseId?: string): IReusableInfo[] | IReusableInfo | undefined--><!--Device-IReusePool-getReusableInfo(componentConstructor : Class,     reuseId?: string): IReusableInfo[] | IReusableInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| componentConstructor | [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md) | Yes |  |
| reuseId | string | No | the reuse-id. |

**Return value:**

| Type | Description |
| --- | --- |
| [IReusableInfo](arkts-utils-ireusableinfo-i.md)[] \| [IReusableInfo](arkts-utils-ireusableinfo-i.md) \| undefined | undefined if this pool does not accepts given Component. returns IReusableInfo if this pool accepts given Component/V2, reuseId was not used to recycle instances returns IReusableInfo[] if this pool accepts given Component/V2, reuseId was used to recycle instances. |

## preRender

```TypeScript
preRender(builder: WrappedBuilder<CustomBuilder>, times: int): Promise<void>
```

The preRender function pre-render n instances and add to pool.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IReusePool-preRender(builder: WrappedBuilder<CustomBuilder>, times: int): Promise<void>--><!--Device-IReusePool-preRender(builder: WrappedBuilder<CustomBuilder>, times: int): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [WrappedBuilder](arkts-builder-wrappedbuilder-c.md)&lt;[CustomBuilder](arkts-custombuilder-t.md)&gt; | Yes | builder a WrappedBuilder containing a @Builder function that accepts no parameter. |
| times | int | Yes | number of times to exec the given @Builder function. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

