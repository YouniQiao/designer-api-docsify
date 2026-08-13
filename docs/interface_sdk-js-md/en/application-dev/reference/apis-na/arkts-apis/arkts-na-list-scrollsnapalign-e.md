# ScrollSnapAlign

Declare limited position when scroll end.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare enum ScrollSnapAlign--><!--Device-unnamed-export declare enum ScrollSnapAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

No alignment. This is the default value.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollSnapAlign-NONE = 0--><!--Device-ScrollSnapAlign-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## START

```TypeScript
START = 1
```

The first item in the view is aligned at the start of the list. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;When the list hits the end, the items at the end must be completely displayed. In this case, the items at the start may not be aligned. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollSnapAlign-START = 1--><!--Device-ScrollSnapAlign-START = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CENTER

```TypeScript
CENTER = 2
```

The middle items in the view are aligned in the center of the list. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;The top and end items can be aligned in the center of the list. In this case, a blank area may result, and the first or last item is aligned to the center of the list. &lt;/pr&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollSnapAlign-CENTER = 2--><!--Device-ScrollSnapAlign-CENTER = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## END

```TypeScript
END = 3
```

The last item in the view is aligned at the end of the list. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;When the list hits the start, the items at the start must be completely displayed. In this case, the items at the end may not be aligned. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollSnapAlign-END = 3--><!--Device-ScrollSnapAlign-END = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

