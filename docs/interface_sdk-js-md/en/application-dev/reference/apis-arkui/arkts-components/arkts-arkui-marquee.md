# Marquee

The **Marquee** component is used to display a scrolling piece of text. Text scrolling is activated only when the content width is greater than or equal to the component's width.

> **NOTE** > > To ensure that scrolling frame rates are not affected, it is recommended that the number of **Marquee** components > in a scroll container does not exceed four, or alternatively, use the Text component's > [TextOverflow.MARQUEE](../arkts-apis/arkts-arkui-textoverflow-e.md) as a substitute. > > For the scenario where the frame rate of the **Marquee** component is dynamic, you can use the > [MarqueeDynamicSyncScene](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) API. > > If the text width is less than the **Marquee** component width, use the property animation to > implement scrolling.

## Child Components

Not supported

## Marquee

```TypeScript
Marquee(options: MarqueeOptions)
```

Creates a marquee.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [MarqueeOptions](arkts-arkui-marqueeoptions-i.md) | Yes | Parameters of the marquee. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [MarqueeOptions](arkts-arkui-marqueeoptions-i.md) | Describes the initialization options of the **Marquee** component. |

## Examples

This example shows the dynamic updating of a marquee's content by setting parameters such as start, step, loop, fromStart, src, and [marqueeUpdateStrategy](#marqueeupdatestrategy12).

```TypeScript
import { LengthMetrics } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct MarqueeExample {
  @State start: boolean = false;
  @State src: string = '';
  @State marqueeText: string = 'Running Marquee';
  private fromStart: boolean = true;
  private step: number = 10;
  private loop: number = Number.POSITIVE_INFINITY;
  controller: TextClockController = new TextClockController();

  convert2time(value: number): string {
    let date = new Date(Number(value + '000'));
    let hours = date.getHours().toString().padStart(2, '0');
    let minutes = date.getMinutes().toString().padStart(2, '0');
    let seconds = date.getSeconds().toString().padStart(2, '0');
    return hours + ":" + minutes + ":" + seconds;
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Marquee({
        start: this.start,
        step: this.step,
        loop: this.loop,
        fromStart: this.fromStart,
        src: this.marqueeText + this.src
      })
        .marqueeUpdateStrategy(MarqueeUpdateStrategy.PRESERVE_POSITION)
        .width('300vp')
        .height('80vp')
        .fontColor('#FFFFFF')
        .fontSize('48fp')
        .allowScale(true) // Set this to true if you want the marquee text to scale with the system font size when using the fp unit for fontSize.
        .fontWeight(700)
        .fontFamily('HarmonyOS Sans') // Use 'HarmonyOS Sans' to avoid following the theme font.
        .backgroundColor('#182431')
        .margin({ bottom: '40vp' })
        .onStart(() => {
          console.info('Succeeded in completing the onStart callback of marquee animation');
        })
        .onBounce(() => {
          console.info('Succeeded in completing the onBounce callback of marquee animation');
        })
        .onFinish(() => {
          console.info('Succeeded in completing the onFinish callback of marquee animation');
        })
      Button('Start')
        .onClick(() => {
          this.start = true
          // Start the text clock.
          this.controller.start();
        })
        .width('120vp')
        .height('40vp')
        .fontSize('16fp')
        .fontWeight(500)
        .backgroundColor('#007DFF')
      TextClock({ timeZoneOffset: -8, controller: this.controller })
        .format('hms')
        .onDateChange((value: number) => {
          this.src = this.convert2time(value);
        })
        .margin('20vp')
        .fontSize('30fp')
    }
    .width('100%')
    .height('100%')
  }
}
```
