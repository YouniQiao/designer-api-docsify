# Stack

The **Stack** component provides a stack container where child components are successively stacked and the latter one overwrites the previous one. > **NOTE** > > - The general attribute align supports the mirroring capability on this component. > > **Child Components** > > Supported

## Stack

```TypeScript
Stack(options?: StackOptions)
```


> **NOTE：**
> 
> Excessive component nesting can lead to performance degradation. In some scenarios, using component attributes
> directly or leveraging system APIs can achieve the same effect as the stack container, reducing the number of
> nested components and optimizing performance. For best practices, see
> [Preferentially Using Component Properties Instead of Nested Components](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-component-nesting-optimization#section78181114123811)
> .

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [StackOptions](arkts-arkui-stackoptions-i.md) | No | Alignment of child components in the container. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [StackOptions](arkts-arkui-stackoptions-i.md) | > **NOTE：**
> 
> To standardize anonymous object definitions, the element definitions here have been revised in API version 18. The
> initial version information of the historical anonymous objects has been retained, which may result in the outer
> element's |

## Examples

When the [alignContent](#aligncontent) attribute of the Stack component is set to Alignment.Bottom and [syncLoad](#syncload) is set to true, the child components are displayed horizontally centered at the bottom of the Stack component, and all child components are loaded within the same frame.

```TypeScript
// xxx.ets
@Entry
@Component
struct StackExample {
  build() {
    // Set the child component to align at the bottom of the Stack container.
    Stack({ alignContent: Alignment.Bottom }) {
      // The first child component, displayed at the bottom.
      Text('First child, show in bottom').width('90%').height('100%').backgroundColor(0xd2cab3).align(Alignment.Top)
      // The second child component, displayed on the upper layer.
      Text('Second child, show in top').width('70%').height('60%').backgroundColor(0xc1cbac).align(Alignment.Top)
    }.width('100%').height(150).margin({ top: 5 })
    // Since API version 26.0.0, the syncLoad attribute is added. Setting it to true means synchronously loading all child components in the Stack area.
    .syncLoad(true)
  }
}
```
