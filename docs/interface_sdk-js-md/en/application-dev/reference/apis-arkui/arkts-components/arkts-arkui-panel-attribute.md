# Panel properties/events

窗格属性。

**Inheritance/Implementation:** PanelAttribute extends [CommonMethod<PanelAttribute>](CommonMethod<PanelAttribute>)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare class PanelAttribute extends CommonMethod<PanelAttribute>--><!--Device-unnamed-declare class PanelAttribute extends CommonMethod<PanelAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundMask

```TypeScript
backgroundMask(color: ResourceColor)
```

指定Panel的背景蒙层。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanelAttribute-backgroundMask(color: ResourceColor): PanelAttribute--><!--Device-PanelAttribute-backgroundMask(color: ResourceColor): PanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | 指定Panel的背景蒙层。 |

## customHeight

```TypeScript
customHeight(value: Dimension | PanelHeight)
```

指定PanelType.CUSTOM状态下的高度。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanelAttribute-customHeight(value: Dimension | PanelHeight): PanelAttribute--><!--Device-PanelAttribute-customHeight(value: Dimension | PanelHeight): PanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| PanelHeight | Yes | 指定PanelType.CUSTOM状态下的高度。 |

## dragBar

```TypeScript
dragBar(value: boolean)
```

设置是否存在控制条。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanelAttribute-dragBar(value: boolean): PanelAttribute--><!--Device-PanelAttribute-dragBar(value: boolean): PanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | 设置是否存在控制条，true表示存在，false表示不存在。 |

## fullHeight

```TypeScript
fullHeight(value: number | string)
```

指定PanelType.Full状态下的高度。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanelAttribute-fullHeight(value: number | string): PanelAttribute--><!--Device-PanelAttribute-fullHeight(value: number | string): PanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string | Yes | 指定PanelMode.Full状态下的高度。 |

## halfHeight

```TypeScript
halfHeight(value: number | string)
```

指定PanelMode.Half状态下的高度。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanelAttribute-halfHeight(value: number | string): PanelAttribute--><!--Device-PanelAttribute-halfHeight(value: number | string): PanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string | Yes | 指定PanelMode.Half状态下的高度。 |

## miniHeight

```TypeScript
miniHeight(value: number | string)
```

指定PanelMode.Mini状态下的高度。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanelAttribute-miniHeight(value: number | string): PanelAttribute--><!--Device-PanelAttribute-miniHeight(value: number | string): PanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string | Yes | 指定PanelMode.Mini状态下的高度。 |

## mode

```TypeScript
mode(value: PanelMode)
```

可滑动面板的初始状态。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanelAttribute-mode(value: PanelMode): PanelAttribute--><!--Device-PanelAttribute-mode(value: PanelMode): PanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PanelMode](arkts-arkui-panelmode-e.md) | Yes | 设置可滑动面板的初始状态。 |

## onChange

```TypeScript
onChange(
    event: (
    /**
     * Width of content area.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     */
    /**
     * Width of content area.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @atomicservice
     * @since 11 dynamiconly
     * @deprecated since 12
     */
      width: number,

    /**
     * Height of content area.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     */
    /**
     * Height of content area.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @atomicservice
     * @since 11 dynamiconly
     * @deprecated since 12
     */
      height: number,

    /**
     * Initial state.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     */
    /**
     * Initial state.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @atomicservice
     * @since 11 dynamiconly
     * @deprecated since 12
     */
      mode: PanelMode,
    ) => void,
  )
```

当可滑动面板发生状态变化时触发。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanelAttribute-onChange(    event: (    /**     * Width of content area.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @since 7     */    /**     * Width of content area.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @FaAndStageModel     * @atomicservice     * @since 11 dynamiconly     * @deprecated since 12     */      width: number,    /**     * Height of content area.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @since 7     */    /**     * Height of content area.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @FaAndStageModel     * @atomicservice     * @since 11 dynamiconly     * @deprecated since 12     */      height: number,    /**     * Initial state.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @since 7     */    /**     * Initial state.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @FaAndStageModel     * @atomicservice     * @since 11 dynamiconly     * @deprecated since 12     */      mode: PanelMode,    ) => void,  ): PanelAttribute--><!--Device-PanelAttribute-onChange(    event: (    /**     * Width of content area.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @since 7     */    /**     * Width of content area.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @FaAndStageModel     * @atomicservice     * @since 11 dynamiconly     * @deprecated since 12     */      width: number,    /**     * Height of content area.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @since 7     */    /**     * Height of content area.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @FaAndStageModel     * @atomicservice     * @since 11 dynamiconly     * @deprecated since 12     */      height: number,    /**     * Initial state.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @since 7     */    /**     * Initial state.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @FaAndStageModel     * @atomicservice     * @since 11 dynamiconly     * @deprecated since 12     */      mode: PanelMode,    ) => void,  ): PanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (     /**      * Width of content area.      *      * @syscap SystemCapability.ArkUI.ArkUI.Full      * @since 7      */     /**      * Width of content area.      *      * @syscap SystemCapability.ArkUI.ArkUI.Full      * @FaAndStageModel      * @atomicservice      * @since 11 dynamiconly      * @deprecated since 12      */       width: number,      /**      * Height of content area.      *      * @syscap SystemCapability.ArkUI.ArkUI.Full      * @since 7      */     /**      * Height of content area.      *      * @syscap SystemCapability.ArkUI.ArkUI.Full      * @FaAndStageModel      * @atomicservice      * @since 11 dynamiconly      * @deprecated since 12      */       height: number,      /**      * Initial state.      *      * @syscap SystemCapability.ArkUI.ArkUI.Full      * @since 7      */     /**      * Initial state.      *      * @syscap SystemCapability.ArkUI.ArkUI.Full      * @FaAndStageModel      * @atomicservice      * @since 11 dynamiconly      * @deprecated since 12      */       mode: PanelMode,     ) =&gt; void | Yes |  |

## onHeightChange

```TypeScript
onHeightChange(callback: (value: number) => void)
```

当可滑动面板发生高度变化时触发。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanelAttribute-onHeightChange(callback: (value: number) => void): PanelAttribute--><!--Device-PanelAttribute-onHeightChange(callback: (value: number) => void): PanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (value: number) =&gt; void | Yes |  |

## show

```TypeScript
show(value: boolean)
```

当滑动面板弹出时调用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanelAttribute-show(value: boolean): PanelAttribute--><!--Device-PanelAttribute-show(value: boolean): PanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | 当滑动面板弹出时调用，true显示面板，false不显示面板。 |

## showCloseIcon

```TypeScript
showCloseIcon(value: boolean)
```

设置是否显示关闭图标。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanelAttribute-showCloseIcon(value: boolean): PanelAttribute--><!--Device-PanelAttribute-showCloseIcon(value: boolean): PanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | 设置是否显示关闭图标，true表示显示，false表示不显示。 |

## type

```TypeScript
type(value: PanelType)
```

可滑动面板的类型。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanelAttribute-type(value: PanelType): PanelAttribute--><!--Device-PanelAttribute-type(value: PanelType): PanelAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PanelType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md) | Yes | 设置可滑动面板的类型。 |

