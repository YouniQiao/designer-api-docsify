# AtomicServiceWeb

为开发者提供满足定制化诉求的Web高阶组件，屏蔽原生Web组件中无需关注的接口，并提供JS扩展能力。

> **说明：**
> 
> - 该组件从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> 
> - 示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Component

<!--Device-unnamed-export declare struct AtomicServiceWeb--><!--Device-unnamed-export declare struct AtomicServiceWeb-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceWeb, OnMessageEvent, OnPageEndEvent, OnHttpErrorReceiveEvent, OnLoadInterceptEvent, WebHeader, OnProgressChangeEvent, OnErrorReceiveEvent, OnPageBeginEvent, OnLoadInterceptCallback, AtomicServiceWebController } from 'kits/@kit.ArkUI';
```

## onLoadIntercept

```TypeScript
onLoadIntercept?: OnLoadInterceptCallback
```

当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。默认允许加载。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-onLoadIntercept?: OnLoadInterceptCallback--><!--Device-AtomicServiceWeb-onLoadIntercept?: OnLoadInterceptCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller: AtomicServiceWebController
```

通过AtomicServiceWebController可以控制AtomicServiceWeb组件各种行为。

**Type:** [AtomicServiceWebController](arkts-arkui-atomicservice-atomicserviceweb-atomicservicewebcontroller-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @ObjectLink

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-controller: AtomicServiceWebController--><!--Device-AtomicServiceWeb-controller: AtomicServiceWebController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## darkMode

```TypeScript
darkMode?: WebDarkMode
```

设置Web深色模式，默认关闭。

**Type:** [WebDarkMode](../../apis-arkweb/arkts-components/arkts-arkweb-webdarkmode-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-darkMode?: WebDarkMode--><!--Device-AtomicServiceWeb-darkMode?: WebDarkMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## forceDarkAccess

```TypeScript
forceDarkAccess?: boolean
```

设置网页是否开启强制深色模式。true表示设置网页开启强制深色模式，false表示设置网页不开启强制深色模式。默认值：false。该属性仅在darkMode开启深色模式时生效。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-forceDarkAccess?: boolean--><!--Device-AtomicServiceWeb-forceDarkAccess?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mixedMode

```TypeScript
mixedMode?: MixedMode
```

设置是否允许加载超文本传输协议（HTTP）和超文本传输安全协议（HTTPS）混合内容，默认不允许加载HTTP和HTTPS混合内容。

**Type:** [MixedMode](../../apis-arkweb/arkts-apis/arkts-arkweb-web-mixedmode-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-mixedMode?: MixedMode--><!--Device-AtomicServiceWeb-mixedMode?: MixedMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navPathStack

```TypeScript
navPathStack?: NavPathStack
```

路由栈信息。当使用NavDestination作为页面的根容器时，需传入NavDestination容器对应的NavPathStack处理页面路由。默认值为空。

**Type:** [NavPathStack](arkts-arkui-navigation-navpathstack-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-navPathStack?: NavPathStack--><!--Device-AtomicServiceWeb-navPathStack?: NavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## nestedScroll

```TypeScript
nestedScroll?: NestedScrollOptions | NestedScrollOptionsExt
```

设置嵌套滚动选项。nestedScroll为NestedScrollOptions（向前、向后两个方向）类型时，scrollForward、scrollBackward默认滚动选项为NestedScrollMode.SELF_FIRST。nestedScroll为NestedScrollOptionsExt（上下左右四个方向）类型时，scrollUp、scrollDown、scrollLeft、scrollRight默认滚动选项为NestedScrollMode.SELF_FIRST。

**Type:** [NestedScrollOptions](arkts-arkui-common-nestedscrolloptions-i.md) \| NestedScrollOptionsExt

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-AtomicServiceWeb-nestedScroll?: NestedScrollOptions | NestedScrollOptionsExt--><!--Device-AtomicServiceWeb-nestedScroll?: NestedScrollOptions | NestedScrollOptionsExt-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onControllerAttached

```TypeScript
onControllerAttached?: Callback<void>
```

当Controller成功绑定到Web组件时触发该回调，此回调中不能使用操作网页的相关接口。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-onControllerAttached?: Callback<void>--><!--Device-AtomicServiceWeb-onControllerAttached?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onErrorReceive

```TypeScript
onErrorReceive?: Callback<OnErrorReceiveEvent>
```

网页加载遇到错误时触发该回调。出于性能考虑，建议此回调中尽量执行简单逻辑。在无网络的情况下，触发此回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;OnErrorReceiveEvent&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-onErrorReceive?: Callback<OnErrorReceiveEvent>--><!--Device-AtomicServiceWeb-onErrorReceive?: Callback<OnErrorReceiveEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHttpErrorReceive

```TypeScript
onHttpErrorReceive?: Callback<OnHttpErrorReceiveEvent>
```

网页加载资源时遇到HTTP错误（响应码>=400）触发该回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;OnHttpErrorReceiveEvent&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-onHttpErrorReceive?: Callback<OnHttpErrorReceiveEvent>--><!--Device-AtomicServiceWeb-onHttpErrorReceive?: Callback<OnHttpErrorReceiveEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onMessage

```TypeScript
onMessage?: Callback<OnMessageEvent>
```

H5页面通过JS SDK的postMessage()发送消息后，Web组件对应的页面返回或销毁时，触发该回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;OnMessageEvent&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-onMessage?: Callback<OnMessageEvent>--><!--Device-AtomicServiceWeb-onMessage?: Callback<OnMessageEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPageBegin

```TypeScript
onPageBegin?: Callback<OnPageBeginEvent>
```

网页开始加载时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;OnPageBeginEvent&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-onPageBegin?: Callback<OnPageBeginEvent>--><!--Device-AtomicServiceWeb-onPageBegin?: Callback<OnPageBeginEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPageEnd

```TypeScript
onPageEnd?: Callback<OnPageEndEvent>
```

网页加载完成时触发该回调，且只在主frame触发。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;OnPageEndEvent&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-onPageEnd?: Callback<OnPageEndEvent>--><!--Device-AtomicServiceWeb-onPageEnd?: Callback<OnPageEndEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onProgressChange

```TypeScript
onProgressChange?: Callback<OnProgressChangeEvent>
```

网页加载进度变化时触发该回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;OnProgressChangeEvent&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-onProgressChange?: Callback<OnProgressChangeEvent>--><!--Device-AtomicServiceWeb-onProgressChange?: Callback<OnProgressChangeEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
src: ResourceStr
```

网页资源地址，访问网络资源需要在AGC（AppGallery Connect）配置业务域名，访问本地资源仅支持包内文件（\$rawfile）。不支持通过状态变量（例如@State）动态更新地址。加载的网页中支持通过JS SDK提供的接口调用系统能力，具体以JS SDK为准。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWeb-src: ResourceStr--><!--Device-AtomicServiceWeb-src: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

