# NavigationInterception

Provide navigation transition interception

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface NavigationInterception--><!--Device-unnamed-export declare interface NavigationInterception-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## didShow

```TypeScript
didShow?: InterceptionShowCallback
```

Called after destination transition.For details, see { @Link InterceptionShowCallback}.

**Type:** [InterceptionShowCallback](arkts-na-interceptionshowcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationInterception-didShow?: InterceptionShowCallback--><!--Device-NavigationInterception-didShow?: InterceptionShowCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## interception

```TypeScript
interception?: InterceptionCallback
```

Called before destination is created.For details, see { @Link InterceptionCallback}.

**Type:** [InterceptionCallback](arkts-na-interceptioncallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationInterception-interception?: InterceptionCallback--><!--Device-NavigationInterception-interception?: InterceptionCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## modeChange

```TypeScript
modeChange?: InterceptionModeCallback
```

Called when navigation mode changed.For details, see { @Link InterceptionModeCallback}.

**Type:** [InterceptionModeCallback](arkts-na-interceptionmodecallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationInterception-modeChange?: InterceptionModeCallback--><!--Device-NavigationInterception-modeChange?: InterceptionModeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## willShow

```TypeScript
willShow?: InterceptionShowCallback
```

Called before destination transition.NavPathStack can be changed in this callback, it will takes effect during this transition.For details, see { @Link InterceptionShowCallback}.

**Type:** [InterceptionShowCallback](arkts-na-interceptionshowcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationInterception-willShow?: InterceptionShowCallback--><!--Device-NavigationInterception-willShow?: InterceptionShowCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

