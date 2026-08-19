# Stack

The **Stack** component provides a stack container where child components are successively stacked and the latter one overwrites the previous one. > **NOTE** > > - The general attribute align supports the mirroring capability on this component. > > **Child Components** > > Supported

## Stack

```TypeScript
Stack(options?: StackOptions)
```

> **NOTE：**&gt; &gt; Excessive component nesting can lead to performance degradation. In some scenarios, using component attributes &gt; directly or leveraging system APIs can achieve the same effect as the stack container, reducing the number of &gt; nested components and optimizing performance. For best practices, see &gt; [Preferentially Using Component Properties Instead of Nested Components](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-component-nesting-optimization#section78181114123811) &gt; .

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-StackInterface-(options?: StackOptions): StackAttribute--><!--Device-StackInterface-(options?: StackOptions): StackAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [StackOptions](arkts-arkui-stackoptions-i.md) | No | Alignment of child components in the container. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [StackOptions](arkts-arkui-stackoptions-i.md) | > **NOTE：**&gt; &gt; To standardize anonymous object definitions, the element definitions here have been revised in API version 18. The &gt; initial version information of the historical anonymous objects has been retained, which may result in the outer &gt; element's @since version number being later than the inner element's version number. However, this does not affect &gt; the use of the API. |

