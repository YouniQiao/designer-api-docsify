# NavigationType

Navigation type.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 13

**Substitutes:** [Navigation](../arkts-apis/arkts-arkui-navigation-navigation-f.md/arkts-arkui-navigation-navigation-f.md#navigation)

<!--Device-unnamed-declare enum NavigationType--><!--Device-unnamed-declare enum NavigationType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Push

```TypeScript
Push
```

Navigates to the specified page in the application.

**NOTE：**

This API is supported since API version 7 and deprecated since API version 13. You are advised to use  
[pushPath](../arkts-apis/arkts-arkui-navigation-navpathstack-c.md/arkts-arkui-navigation-navpathstack-c.md#pushpath) instead.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 13

**Substitutes:** [NavPathStack#pushPath](../arkts-apis/arkts-arkui-navigation-navpathstack-c.md/arkts-arkui-navigation-navpathstack-c.md#pushpath)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigationType-Push--><!--Device-NavigationType-Push-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Back

```TypeScript
Back
```

Returns to the specified page. If the specified page does not exist in the stack, no response is returned. If no page is specified, the previous page is returned to.

**NOTE：**

This API is supported since API version 7 and deprecated since API version 13. You are advised to use  
[pop](../arkts-apis/arkts-arkui-navigation-navpathstack-c.md/arkts-arkui-navigation-navpathstack-c.md#pop) instead.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 13

**Substitutes:** [NavPathStack#pop](../arkts-apis/arkts-arkui-navigation-navpathstack-c.md/arkts-arkui-navigation-navpathstack-c.md#pop)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigationType-Back--><!--Device-NavigationType-Back-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Replace

```TypeScript
Replace
```

Replaces the current page with another one in the application and destroys the current page.

**NOTE：**

This API is supported since API version 7 and deprecated since API version 13. You are advised to use  
[replacePath](../arkts-apis/arkts-arkui-navigation-navpathstack-c.md/arkts-arkui-navigation-navpathstack-c.md#replacepath) instead.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 13

**Substitutes:** [NavPathStack.replacePath](../arkts-apis/arkts-arkui-navigation-navpathstack-c.md/arkts-arkui-navigation-navpathstack-c.md#replacepath)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigationType-Replace--><!--Device-NavigationType-Replace-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

