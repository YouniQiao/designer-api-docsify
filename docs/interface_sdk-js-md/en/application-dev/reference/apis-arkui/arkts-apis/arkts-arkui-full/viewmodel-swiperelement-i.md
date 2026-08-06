# SwiperElement

The \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ component provides a swiper container.

**Inheritance/Implementation:** SwiperElement extends [Element](viewmodel-element-i.md)

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

<!--Device-unnamed-export interface SwiperElement extends Element--><!--Device-unnamed-export interface SwiperElement extends Element-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showNext

```TypeScript
showNext(): void
```

Shows the next child component.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-SwiperElement-showNext(): void--><!--Device-SwiperElement-showNext(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showPrevious

```TypeScript
showPrevious(): void
```

Shows the previous child component.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-SwiperElement-showPrevious(): void--><!--Device-SwiperElement-showPrevious(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## swipeTo

```TypeScript
swipeTo(position: {
    /**
     * specified position.
     *
     * @type { number }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @famodelonly
     * @since 4 dynamiconly
     */
    index: number;
  }): void
```

Scrolls the child component to the position at the specified index.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-SwiperElement-swipeTo(position: {    /**     * specified position.     *     * @type { number }     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @famodelonly     * @since 4 dynamiconly     */    index: number;  }): void--><!--Device-SwiperElement-swipeTo(position: {    /**     * specified position.     *     * @type { number }     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @famodelonly     * @since 4 dynamiconly     */    index: number;  }): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | {     /**      * specified position.      *      * @type { number }      * @syscap SystemCapability.ArkUI.ArkUI.Full      * @famodelonly      * @since 4 dynamiconly      */     index: number;   } | Yes |  |

