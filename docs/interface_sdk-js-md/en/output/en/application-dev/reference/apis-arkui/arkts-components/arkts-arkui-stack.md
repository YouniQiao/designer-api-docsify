# Stack

The **Stack** component provides a stack container where child components are successively stacked and the latter one overwrites the previous one. > **NOTE** > > - The general attribute [align]{@link CommonMethod#align} supports the mirroring capability on this component. > > **Child Components** > > Supported

## Stack

```TypeScript
Stack(options?: StackOptions)
```

> **NOTE** > > Excessive component nesting can lead to performance degradation. In some scenarios, using component attributes > directly or leveraging system APIs can achieve the same effect as the stack container, reducing the number of > nested components and optimizing performance. For best practices, see > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ > .

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-StackInterface-(options?: StackOptions): StackAttribute--><!--Device-StackInterface-(options?: StackOptions): StackAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Alignment of child components in the container. |

## Summary

