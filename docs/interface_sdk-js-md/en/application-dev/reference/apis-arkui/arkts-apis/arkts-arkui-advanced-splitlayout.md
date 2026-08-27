# @ohos.arkui.advanced.SplitLayout

## Modules to Import

```TypeScript
import { SplitLayout } from '@kit.ArkUI';
```

## Summary

### Structs

| Name | Description |
| --- | --- |
| [SplitLayout](arkts-arkui-arkui-advanced-splitlayout-splitlayout-s.md) | Declare SplitLayout.The SplitLayout is used for upper and lower graphic layouts. |

## Examples

This example demonstrates how to use SplitLayout to achieve a page layout that is both adaptable and responsive.

```TypeScript
import { SplitLayout } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State demoImage: Resource = $r('app.media.background');

  build() {
    Column() {
      SplitLayout({
        mainImage: this.demoImage,
        primaryText:'New music recommendation',
        secondaryText: 'Get a playlist tailored to your taste;',
        tertiaryText: 'Updated every day',
      }) {
        Text('Example: Components can be added to a blank area container.')
          .margin({ top: 36 })
      }
    }
    .justifyContent(FlexAlign.SpaceBetween)
    .height('100%')
    .width('100%')
  }
}
```
