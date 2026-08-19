# on_tabContentUpdate

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## on('tabContentUpdate')

```TypeScript
export function on(type: 'tabContentUpdate', options: ObserverOptions, callback: Callback<TabContentInfo>): void
```

Subscribes to **TabContent** page switching events for the specified **Tabs** component identified by its ID. Unlike [on('tabChange')](arkts-arkui-arkui-uicontext-uiobserver-c.md#onnavdestinationupdate), this API does not support listening for the initial tab display event when the **Tabs** component is initialized.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function on(type: 'tabContentUpdate', options: ObserverOptions, callback: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function on(type: 'tabContentUpdate', options: ObserverOptions, callback: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'tabContentUpdate' | Yes | Event type. Set to **'tabContentUpdate'** for **TabContent** page switching events. |
| options | ObserverOptions | Yes | ID of the target **Tabs** component. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[TabContentInfo](../../apis-na/arkts-apis/arkts-na-uiobserver-tabcontentinfo-i.md)&gt; | Yes | Callback used to return the result. It provides information about **TabContent** switch events through **TabContentInfo**. |

**Examples**

```TypeScript
import { uiObserver } from '@kit.ArkUI';

function callbackFunc(info: uiObserver.TabContentInfo) {
  console.info(`tabContentUpdate ${JSON.stringify(info)}`);
}

@Entry
@Component
struct TabsExample {

  aboutToAppear(): void {
    // Register a listener with the specified tab ID.
    uiObserver.on('tabContentUpdate', { id: 'tabsId' }, callbackFunc);
  }

  aboutToDisappear(): void {
    // Unregister the listeners.
    uiObserver.off('tabContentUpdate', { id: 'tabsId' }, callbackFunc);
  }

  build() {
    Column() {
      Tabs() {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#00CB87')
        }.tabBar('green').id('tabContentId0')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#007DFF')
        }.tabBar('blue').id('tabContentId1')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#FFBF00')
        }.tabBar('yellow').id('tabContentId2')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#E67C92')
        }.tabBar('pink').id('tabContentId3')
      }
      .width(360)
      .height(296)
      .backgroundColor('#F1F3F5')
      .id('tabsId')
    }.width('100%')
  }
}
```


## on('tabContentUpdate')

```TypeScript
export function on(type: 'tabContentUpdate', callback: Callback<TabContentInfo>): void
```

Subscribes to **TabContent** switch events. Unlike [on('tabChange')](arkts-arkui-arkui-uicontext-uiobserver-c.md#onnavdestinationupdate), this API does not support listening for the initial tab display event when the **Tabs** component is initialized.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function on(type: 'tabContentUpdate', callback: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function on(type: 'tabContentUpdate', callback: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'tabContentUpdate' | Yes | Event type. Set to **'tabContentUpdate'** for **TabContent** page switching events. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[TabContentInfo](../../apis-na/arkts-apis/arkts-na-uiobserver-tabcontentinfo-i.md)&gt; | Yes | Callback used to return the result. It provides information about **TabContent** switch events through **TabContentInfo**. |

**Examples**

```TypeScript
import { uiObserver } from '@kit.ArkUI';

function callbackFunc(info: uiObserver.TabContentInfo) {
  console.info(`tabContentUpdate ${JSON.stringify(info)}`);
}

@Entry
@Component
struct TabsExample {

  aboutToAppear(): void {
    // Register a listener.
    uiObserver.on('tabContentUpdate', callbackFunc);
  }

  aboutToDisappear(): void {
    // Unregister the listeners.
    uiObserver.off('tabContentUpdate', callbackFunc);
  }

  build() {
    Column() {
      Tabs() {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#00CB87')
        }.tabBar('green').id('tabContentId0')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#007DFF')
        }.tabBar('blue').id('tabContentId1')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#FFBF00')
        }.tabBar('yellow').id('tabContentId2')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#E67C92')
        }.tabBar('pink').id('tabContentId3')
      }
      .width(360)
      .height(296)
      .backgroundColor('#F1F3F5')
      .id('tabsId')
    }.width('100%')
  }
}
```

