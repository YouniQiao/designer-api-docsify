# InnerFullScreenLaunchComponent (System API)

InnerFullScreenLaunchComponent** is a component that allows the invoker to choose the timing for launching an atomic service. If the invoked app (the one being launched) grants the invoker the authorization to run the atomic service in an embedded manner, the invoker can operate the atomic service in full-screen embedded mode. If authorization is not provided, the invoker will launch the atomic service in a pop-up manner.
    **NOTE**  
    
    To implement an embeddable atomic service within this component, it must inherit from  
    [EmbeddableUIAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. If it does not inherit from  
    **EmbeddableUIAbility**, the system cannot guarantee that the atomic service will function properly.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Component

<!--Device-unnamed-export declare struct InnerFullScreenLaunchComponent--><!--Device-unnamed-export declare struct InnerFullScreenLaunchComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## content

```TypeScript
content: Callback<void>
```

Content displayed in the component.

**Type:** Callback&lt;void&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @BuilderParam

<!--Device-InnerFullScreenLaunchComponent-content: Callback<void>--><!--Device-InnerFullScreenLaunchComponent-content: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## controller

```TypeScript
controller: LaunchController
```

Controller for launching the atomic service.

**Type:** LaunchController

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-InnerFullScreenLaunchComponent-controller: LaunchController--><!--Device-InnerFullScreenLaunchComponent-controller: LaunchController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## onError

```TypeScript
onError?: ErrorCallback
```

Callback triggered when an exception occurs during the execution of an embedded atomic service. You can obtain the error information based on the **code**, **name**, and **message** parameters in the callback and rectify the exception accordingly.

**Type:** ErrorCallback

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-InnerFullScreenLaunchComponent-onError?: ErrorCallback--><!--Device-InnerFullScreenLaunchComponent-onError?: ErrorCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## onReceive

```TypeScript
onReceive?: Callback<Record<string, Object>>
```

Callback triggered when an embedded atomic service calls [@ohos.window (window)]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ APIs.

**Type:** Callback&lt;Record&lt;string, Object&gt;&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-InnerFullScreenLaunchComponent-onReceive?: Callback<Record<string, Object>>--><!--Device-InnerFullScreenLaunchComponent-onReceive?: Callback<Record<string, Object>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## onTerminated

```TypeScript
onTerminated?: Callback<TerminationInfo>
```

Callback triggered when an embedded atomic service exits normally. Exit scenarios include user-triggered exit button taps or edge swipes, or calls to  
[terminateSelfWithResult]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_or  
[terminateSelf]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Type:** Callback&lt;TerminationInfo&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-InnerFullScreenLaunchComponent-onTerminated?: Callback<TerminationInfo>--><!--Device-InnerFullScreenLaunchComponent-onTerminated?: Callback<TerminationInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

