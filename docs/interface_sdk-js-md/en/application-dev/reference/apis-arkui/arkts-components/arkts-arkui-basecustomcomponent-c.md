# BaseCustomComponent

Custom Component base class and it is migrated from class CustomComponent.

**Inheritance/Implementation:** BaseCustomComponent extends [CommonAttribute](arkts-arkui-common-attribute.md#commonattribute)

**Since:** 18

<!--Device-unnamed-declare class BaseCustomComponent--><!--Device-unnamed-declare class BaseCustomComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## aboutToAppear

```TypeScript
aboutToAppear?(): void
```

aboutToAppear Method and it is migrated from class CustomComponent.

The aboutToAppear function is executed after a new instance of the custom component is created, before its build() function is executed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BaseCustomComponent-aboutToAppear?(): void--><!--Device-BaseCustomComponent-aboutToAppear?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToDisappear

```TypeScript
aboutToDisappear?(): void
```

aboutToDisappear Method and it is migrated from class CustomComponent.

The aboutToDisappear function executes before a custom component is destroyed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BaseCustomComponent-aboutToDisappear?(): void--><!--Device-BaseCustomComponent-aboutToDisappear?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToRecycle

```TypeScript
aboutToRecycle?(): void
```

aboutToRecycle Method and it is migrated from class CustomComponent.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BaseCustomComponent-aboutToRecycle?(): void--><!--Device-BaseCustomComponent-aboutToRecycle?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
import { ComponentInit, ComponentDisappear, UIUtils, CustomComponentLifecycleObserver, CustomComponentLifecycle } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export class Message {
  value: string | undefined;
  constructor(value: string) {
    this.value = value;
  }
}

@Entry
@Component
struct Index {
  @State switch: boolean = true;

  build() {
    Column() {
      Button('Hello')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.switch = !this.switch;
        })
      if (this.switch) {
        // If only one reusable component is used, reuseId is optional.
        Child({ message: new Message('Child') })
          .reuseId('Child')
      }
    }
    .height('100%')
    .width('100%')
  }
}

@Reusable
@Component
struct Child {
  @State message: Message = new Message('AboutToReuse');
  @State label: string = 'HelloWorld';
  @ComponentInit
  myInit(): void {
    registerObserver(UIUtils.getLifecycle(this));
  }
  @ComponentDisappear
  myDisappear(): void {
    unRegisterObserver(UIUtils.getLifecycle(this));
  }
  build() {
    Column() {
      Text(this.message.value)
        .fontSize(30)
    }
  }
}

export class MyObserver implements CustomComponentLifecycleObserver {
  // Override the lifecycle events in CustomComponentLifecycleObserver. CustomComponentLifecycleObserver cannot listen to the aboutToInit event of the parent component.
  aboutToAppear() {
    hilog.info(0x0000, 'testTag', 'MyObserver aboutToAppear');
  }
  onDidBuild() {
    hilog.info(0x0000, 'testTag', 'MyObserver onDidBuild');
  }
  aboutToAttach() {
    hilog.info(0x0000, 'testTag', 'MyObserver aboutToAttach');
  }
  aboutToDetach() {
    hilog.info(0x0000, 'testTag', 'MyObserver aboutToDetach');
  }
  aboutToReuse(param?: ESObject) {
    // The value of param is not undefined in the reuse callback of the V1 component and is undefined in the reuse callback of the V2 component.
    hilog.info(0x0000, 'testTag', 'MyObserver aboutToReuse');
  }
  aboutToRecycle() {
    hilog.info(0x0000, 'testTag', 'MyObserver aboutToRecycle');
  }
  // Unregister the listener in the aboutToDelete function of the parent component. As a result, the aboutToDisappear event of the parent component cannot be listened to.
  aboutToDisappear() {
    hilog.info(0x0000, 'testTag', 'MyObserver aboutToDisappear');
  }
}

// Create the Observer object.
const observer = new MyObserver();

export function registerObserver(lifeCycle: CustomComponentLifecycle) {
  // Register the listener with lifeCycle.
  lifeCycle.addObserver(observer);
}

export function unRegisterObserver(lifeCycle: CustomComponentLifecycle) {
  // Unregister the listener from lifeCycle.
  lifeCycle.removeObserver(observer);
}
```

## build

```TypeScript
build(): void
```

Customize the pop-up content constructor and it is migrated from class CustomComponent.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BaseCustomComponent-build(): void--><!--Device-BaseCustomComponent-build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getDialogController

```TypeScript
getDialogController(): PromptActionDialogController | undefined
```

The dialog controller of the custom component.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-BaseCustomComponent-getDialogController(): PromptActionDialogController | undefined--><!--Device-BaseCustomComponent-getDialogController(): PromptActionDialogController | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PromptActionDialogController](arkts-arkui-promptactiondialogcontroller-t.md) \| undefined | The controller of dialog, or undefined if it is not available |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { ComponentContent } from '@kit.ArkUI';

class Params {
  text: string = "";
  constructor(text: string) {
    this.text = text;
  }
}

@ComponentV2
struct MyComponent {
  build() {
    Column() {
      Button('Close Dialog')
        .onClick(() => {
          let ctrl: PromptActionDialogController = this.getDialogController();
          if (ctrl != undefined) {
            ctrl.close();
          }
        })
    }
  }
}

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(50)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 36 })
    MyComponent()
  }.backgroundColor('#FFF0F0F0')
}

@Entry
@ComponentV2
struct Index {
  @Local message: string = "hello";

  build() {
    Row() {
      Column({ space: 10 }) {
        Button('click me')
          .fontSize(20)
          .onClick(() => {
            let ctx = this.getUIContext();
            let promptAction = ctx.getPromptAction();
            promptAction.openCustomDialog(new ComponentContent(ctx, wrapBuilder(buildText), new Params(this.message)))
              .catch((err: BusinessError) => {
                console.error("openCustomDialog error: " + err.code + " " + err.message);
              })
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```

## getUIContext

```TypeScript
getUIContext(): UIContext
```

Get current UIContext and it is migrated from class CustomComponent.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseCustomComponent-getUIContext(): UIContext--><!--Device-BaseCustomComponent-getUIContext(): UIContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](arkts-arkui-uicontext-t.md) | The UIContext that the custom component belongs to. |

## getUniqueId

```TypeScript
getUniqueId(): number
```

Get uniqueId of the custom component and it is migrated from class CustomComponent.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseCustomComponent-getUniqueId(): number--><!--Device-BaseCustomComponent-getUniqueId(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | The uniqueId of the custom component. |

**Examples**

```TypeScript
@Entry
@Component
struct MyComponent {
  aboutToAppear() {
    let uniqueId: number = this.getUniqueId();
  }

  build() {
    // ...
  }
}
```

## onBackPress

```TypeScript
onBackPress?(): void | boolean
```

Invoked when a user clicks the back button on a router-managed page (a custom component decorated with [\@Entry](../../../ui/state-management/arkts-create-custom-components.md#entry)). The value **true** means that the page executes its own return logic, and **false** (default) means that the default return logic is used.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BaseCustomComponent-onBackPress?(): void | boolean--><!--Device-BaseCustomComponent-onBackPress?(): void | boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidBuild

```TypeScript
onDidBuild?(): void
```

The callback method after the custom component is built and it is migrated from class CustomComponent.

Triggered when the custom component has been built.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseCustomComponent-onDidBuild?(): void--><!--Device-BaseCustomComponent-onDidBuild?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onFormRecover

```TypeScript
onFormRecover?(statusData: string): void
```

onFormRecover Method, this is only for ArkTS form, it is migrated from class CustomComponent.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-BaseCustomComponent-onFormRecover?(statusData: string): void--><!--Device-BaseCustomComponent-onFormRecover?(statusData: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| statusData | string | Yes | indicate status data of ArkTS form UI, which is acquired by calling onFormRecycle, it is used to recover form |

**Examples**

```TypeScript
@Entry
@Component
struct WidgetCard {
  readonly title: string = 'Hello World';
  readonly actionType: string = 'router';
  readonly abilityName: string = 'EntryAbility';
  readonly message: string = 'add detail';
  readonly fullWidthPercent: string = '100%';
  readonly fullHeightPercent: string = '100%';

  onFormRecycle(): string {
    let formId: string = "1859635745"
    console.info("card is recycled, formID: " + formId);
    return formId;
  }

  onFormRecover(statusData: string): void {
    console.info("card has been restored, formID: " + statusData);
  }

  build() {
    Row() {
      Column() {
        Text(this.title)
          .fontSize($r('app.float.font_size'))
          .fontWeight(FontWeight.Medium)
          .fontColor($r('sys.color.font'))
      }
      .width(this.fullWidthPercent)
    }
    .height(this.fullHeightPercent)
    .backgroundColor($r('sys.color.comp_background_primary'))
    .onClick(() => {
      postCardAction(this, {
        action: this.actionType,
        abilityName: this.abilityName,
        params: {
          message: this.message
        }
      });
    })
  }
}
```

## onFormRecycle

```TypeScript
onFormRecycle?(): string
```

onFormRecycle Method, this is only for ArkTS form, if form was marked recyclable by form user, when system memory is low, it will be recycled after calling this method, you should return a string of params that you wish to be saved, it will be passed back as params in onFormRecover, in which you can recover the form, it is migrated from class CustomComponent.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-BaseCustomComponent-onFormRecycle?(): string--><!--Device-BaseCustomComponent-onFormRecycle?(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | status data of ArkTS form UI, this data will be passed in when recover form later |

**Examples**

```TypeScript
@Entry
@Component
struct WidgetCard {
  readonly title: string = 'Hello World';
  readonly actionType: string = 'router';
  readonly abilityName: string = 'EntryAbility';
  readonly message: string = 'add detail';
  readonly fullWidthPercent: string = '100%';
  readonly fullHeightPercent: string = '100%';

  onFormRecycle(): string {
    let formId: string = "1859635745"
    console.info("card is recycled, formID: " + formId);
    return formId;
  }

  onFormRecover(statusData: string): void {
    console.info("card has been restored, formID: " + statusData);
  }

  build() {
    Row() {
      Column() {
        Text(this.title)
          .fontSize($r('app.float.font_size'))
          .fontWeight(FontWeight.Medium)
          .fontColor($r('sys.color.font'))
      }
      .width(this.fullWidthPercent)
    }
    .height(this.fullHeightPercent)
    .backgroundColor($r('sys.color.comp_background_primary'))
    .onClick(() => {
      postCardAction(this, {
        action: this.actionType,
        abilityName: this.abilityName,
        params: {
          message: this.message
        }
      });
    })
  }
}
```

## onMeasureSize

```TypeScript
onMeasureSize?(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions): SizeResult
```

Invoked when the custom component needs to determine its size. Through this callback the component receives its layout information and size constraints from the ArkUI framework. State variables should not be changed in this callback.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BaseCustomComponent-onMeasureSize?(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions): SizeResult--><!--Device-BaseCustomComponent-onMeasureSize?(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions): SizeResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selfLayoutInfo | [GeometryInfo](arkts-arkui-geometryinfo-i.md) | Yes | Information about the component's computed layout properties after measurement.<br>During the first layout, the component will use its own set attributes as the basis for layout. |
| children | Array&lt;[Measurable](arkts-arkui-measurable-i.md)&gt; | Yes | Array containing layout information for all child components after measurement. <br>When a child component does not have its layout information set, it retains the previous layout settings or, if no previous layout settings are available, stays at the default size of 0. |
| constraint | ConstraintSizeOptions | Yes | Layout constraints applied to the component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SizeResult](arkts-arkui-sizeresult-i.md) | Component size information. |

## onNewParam

```TypeScript
onNewParam?(param: ESObject): void
```

Triggered when the Entry custom component has been pushed with singleton mode.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-BaseCustomComponent-onNewParam?(param: ESObject): void--><!--Device-BaseCustomComponent-onNewParam?(param: ESObject): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [ESObject](../../apis-default/arkts-apis/arkts-esobject-t.md) | Yes | New parameters pushed with singleton mode. |

## onPageHide

```TypeScript
onPageHide?(): void
```

Invoked each time a router-managed page (a custom component decorated with [\@Entry](../../../ui/state-management/arkts-create-custom-components.md#entry)) is hidden, including scenarios such as route navigation and the application moving to the background.

> **NOTE：**

> To ensure smooth UI responsiveness, avoid executing time-consuming operations within the callback function that
> may block the main thread. For resource-intensive tasks such as camera resource deallocation, consider
> implementing asynchronous solutions. For best practices, see
> [Reducing Application Latency: Postponing Resource Release](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-application-latency-optimization-cases#section8783201923819).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BaseCustomComponent-onPageHide?(): void--><!--Device-BaseCustomComponent-onPageHide?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPageShow

```TypeScript
onPageShow?(): void
```

Invoked each time a router-managed page (a custom component decorated with [\@Entry](../../../ui/state-management/arkts-create-custom-components.md#entry)) is displayed, including scenarios such as route navigation and the application returning to the foreground.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BaseCustomComponent-onPageShow?(): void--><!--Device-BaseCustomComponent-onPageShow?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPlaceChildren

```TypeScript
onPlaceChildren?(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void
```

Invoked when the custom component needs to determine the positions of its child components. Through this callback the component receives its child component size constraints from the ArkUI framework. State variables should not be changed in this callback.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BaseCustomComponent-onPlaceChildren?(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void--><!--Device-BaseCustomComponent-onPlaceChildren?(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selfLayoutInfo | [GeometryInfo](arkts-arkui-geometryinfo-i.md) | Yes | Information about the component's computed layout properties after measurement. |
| children | Array&lt;[Layoutable](arkts-arkui-layoutable-i.md)&gt; | Yes | Array containing layout information for all child components after measurement. |
| constraint | ConstraintSizeOptions | Yes | Layout constraints applied to the component. |

**Examples**

See the [example for customizing a layout](#example).

## onWillApplyTheme

```TypeScript
onWillApplyTheme?(theme: Theme): void
```

Invoked before the **build()** function of a new instance of the custom component is executed, to obtain the **Theme** object of the component context. You can change state variables in **onWillApplyTheme**. The change will take effect when you execute the **build()** function next time.

> Note:
> Since API version 18, this API can be used in the status management V2 component.

> **NOTE：**

> Since API version 18, this API is supported in the components of V2.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseCustomComponent-onWillApplyTheme?(theme: Theme): void--><!--Device-BaseCustomComponent-onWillApplyTheme?(theme: Theme): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| theme | [Theme](arkts-arkui-theme-t.md) | Yes | Current theme object of the custom component. |

## pageTransition

```TypeScript
pageTransition?(): void
```

PageTransition Method and it is migrated from class CustomComponent. Implement Animation when enter this page or move to other pages.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BaseCustomComponent-pageTransition?(): void--><!--Device-BaseCustomComponent-pageTransition?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## queryNavDestinationInfo

```TypeScript
queryNavDestinationInfo(): NavDestinationInfo | undefined
```

Queries the **NavDestination** information of this custom component. This API has effect only when the component is contained within a **NavDestination** component.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseCustomComponent-queryNavDestinationInfo(): NavDestinationInfo | undefined--><!--Device-BaseCustomComponent-queryNavDestinationInfo(): NavDestinationInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NavDestinationInfo](arkts-arkui-navdestinationinfo-t.md) \| undefined | NavDestinationInfo** instance obtained. |

**Examples**

```TypeScript
import { uiObserver } from '@kit.ArkUI';

@Component
export struct NavDestinationExample {
  build() {
    NavDestination() {
      MyComponent()
    }
  }
}

@Component
struct MyComponent {
  navDesInfo: uiObserver.NavDestinationInfo | undefined

  aboutToAppear() {
    // this refers to the custom node MyComponent and searches for the nearest parent node of the NavDestination type from this node upwards.
    this.navDesInfo = this.queryNavDestinationInfo();
    console.info('get navDestinationInfo: ' + JSON.stringify(this.navDesInfo));
  }

  build() {
    // ...
  }
}
```

```TypeScript
// Index.ets
@Entry
@Component
struct NavigationExample {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pageInfo) {
      Column() {
        Button('pageOne', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfo.pushPath({ name: 'pageOne' }); // Push the navigation destination page specified by name to the navigation stack.
          })
      }
    }.title('NavIndex')
  }
}
```

```TypeScript
// PageOne.ets
import { uiObserver } from '@kit.ArkUI';

@Builder
export function PageOneBuilder() {
  PageOneComponent()
}

@Component
export struct PageOneComponent {
  navDesInfo: uiObserver.NavDestinationInfo | undefined;
  @State text: string = '';
  build() {
    NavDestination() {
      Column() {
        Button('Search Inward')
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            // Search inward for the NavDestination information for PageOne.
            this.navDesInfo = this.queryNavDestinationInfo(true);
            this.text = JSON.stringify(this.navDesInfo?.name).toString();
          })
        Text('The NavDestination component found inward is:' + this.text)
          .width('80%')
          .height(50)
          .margin(50)
          .fontSize(20)
        MyComponent()
      }.width('100%').height('100%')
    }
    .title('pageOne')
  }
}

@Component
struct MyComponent {
  navDesInfo: uiObserver.NavDestinationInfo | undefined;
  @State text: string = '';

  build() {
    Column() {
      Button('Search Outward')
        .width('80%')
        .height(40)
        .margin(20)
        .onClick(() => {
          // Search outward for the NavDestination information for PageOne.
          this.navDesInfo = this.queryNavDestinationInfo(false);
          this.text = JSON.stringify(this.navDesInfo?.name).toString();
        })
      Text('The NavDestination component found outward is:' + this.text)
        .width('80%')
        .height(50)
        .margin(50)
        .fontSize(20)
    }
  }
}
```

```TypeScript
//route_map.json
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  ]
}
```

## queryNavDestinationInfo

```TypeScript
queryNavDestinationInfo(isInner: Optional<boolean>): NavDestinationInfo | undefined
```

Queries the information of the nearest **NavDestination** component (a navigation page or subpage of the **Navigation** component) associated with this custom component. The search direction is controlled by **isInner**: **true** for inward search and **false** for outward search.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-BaseCustomComponent-queryNavDestinationInfo(isInner: Optional<boolean>): NavDestinationInfo | undefined--><!--Device-BaseCustomComponent-queryNavDestinationInfo(isInner: Optional<boolean>): NavDestinationInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isInner | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | Whether to search inward for the nearest **NavDestination** component in the navigation stack.<br>**true**: Search inward.<br>**false**: Search outward. |

**Return value:**

| Type | Description |
| --- | --- |
| [NavDestinationInfo](arkts-arkui-navdestinationinfo-t.md) \| undefined | NavDestinationInfo** instance obtained. |

**Examples**

See [queryNavDestinationInfo](#querynavdestinationinfo)

## queryNavigationInfo

```TypeScript
queryNavigationInfo(): NavigationInfo | undefined
```

Queries the **Navigation** information of this custom component.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseCustomComponent-queryNavigationInfo(): NavigationInfo | undefined--><!--Device-BaseCustomComponent-queryNavigationInfo(): NavigationInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationInfo](arkts-arkui-navigationinfo-t.md) \| undefined | NavigationInfo** instance obtained. |

**Examples**

```TypeScript
// index.ets
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct MainPage {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pathStack) {
      // ...
    }.id("NavigationId")
  }
}


@Component
export struct PageOne {
  pathStack: NavPathStack = new NavPathStack();

  aboutToAppear() {
    // this refers to the custom node PageOne and searches for the nearest parent node of the Navigation type from this node upwards.
    let navigationInfo: uiObserver.NavigationInfo | undefined = this.queryNavigationInfo();
    console.info('get navigationInfo: ' + JSON.stringify(navigationInfo));
    if (navigationInfo !== undefined) {
      this.pathStack = navigationInfo.pathStack;
    }
  }

  build() {
    NavDestination() {
      // ...
    }.title('PageOne')
  }
}
```

## queryRouterPageInfo

```TypeScript
queryRouterPageInfo(): RouterPageInfo | undefined
```

Obtains a **RouterPageInfo** instance.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseCustomComponent-queryRouterPageInfo(): RouterPageInfo | undefined--><!--Device-BaseCustomComponent-queryRouterPageInfo(): RouterPageInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RouterPageInfo](arkts-arkui-routerpageinfo-t.md) \| undefined | RouterPageInfo** instance obtained. |

**Examples**

```TypeScript
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct MyComponent {
  aboutToAppear() {
    let info: uiObserver.RouterPageInfo | undefined = this.queryRouterPageInfo();
  }

  build() {
    // ...
  }
}
```

