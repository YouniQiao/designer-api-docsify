# NavigationInterception

Navigation跳转拦截对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavigationInterception--><!--Device-unnamed-export declare interface NavigationInterception-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## didShow

```TypeScript
didShow?: InterceptionShowCallback
```

页面跳转后回调。在该回调中操作栈在下一次跳转中刷新。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationInterception-didShow?: InterceptionShowCallback--><!--Device-NavigationInterception-didShow?: InterceptionShowCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## interception

```TypeScript
interception?: InterceptionCallback
```

页面跳转前的回调，允许操作栈，在当前跳转中生效。拦截的页面不会被创建。

**模型约束：** 此接口仅可在Stage模型下使用。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationInterception-interception?: InterceptionCallback--><!--Device-NavigationInterception-interception?: InterceptionCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## modeChange

```TypeScript
modeChange?: InterceptionModeCallback
```

Navigation单双栏显示状态发生变更时触发该回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationInterception-modeChange?: InterceptionModeCallback--><!--Device-NavigationInterception-modeChange?: InterceptionModeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## willShow

```TypeScript
willShow?: InterceptionShowCallback
```

页面跳转前的回调，允许操作栈，在当前跳转中生效。拦截的页面会被创建。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationInterception-willShow?: InterceptionShowCallback--><!--Device-NavigationInterception-willShow?: InterceptionShowCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

