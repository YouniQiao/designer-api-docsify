# Navigator

路由容器组件，提供路由跳转能力。

> **说明：**

## 子组件

可以包含子组件。

## Navigator

```TypeScript
Navigator(value?: { target: string; type?: NavigationType })
```

在路由跳转时调用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 13

**Substitutes:** <!--SUBSTITUTE_API-->NavPathInfo<!--/SUBSTITUTE_API-->

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigatorInterface-(value?: { target: string; type?: NavigationType }): NavigatorAttribute--><!--Device-NavigatorInterface-(value?: { target: string; type?: NavigationType }): NavigatorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { target: string; type?: NavigationType } | No | 跳转页面的信息。<br/>target：指定跳转目标页面的路径。<br/>type：指定路由方式。<br/>默认值：NavigationType.Push |

## Navigator

```TypeScript
Navigator()
```

在使用Navigator时调用。

NavigationAttribute为Navigation组件的属性。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 13

**Substitutes:** <!--SUBSTITUTE_API-->NavigationAttribute<!--/SUBSTITUTE_API-->

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigatorInterface-(): NavigatorAttribute--><!--Device-NavigatorInterface-(): NavigatorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

- [NavigationType](arkts-arkui-navigator-navigationtype-e.md)
