# SlideRange

Defines the callback type used in SlideRange. <p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Currently, this API takes effect only when MIN ≤ from ≤ to ≤ MAX (the values of MIN and MAX do not depend on the values set, but on the actual values that take effect). You can set either from or to, or you can set both from and to. When the API is effective, if the set from value is between the adjacent multiples of step, then from takes the value of the left interval multiple of step or MIN as the corrected value. When the API is effective, if the set to value is between the adjacent multiples of step, then to takes the value of the right interval multiple of step or MAX as the corrected value. After from and to have taken their corrected values, when value is undefined or null, it takes the same value as from; when value is a number type, and if value ≤ from, then it takes from; if value &gt; to, then it takes to. </p>@interface SlideRange

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## from

```TypeScript
from?: double
```

Start of the slide range.

**Type:** double

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## to

```TypeScript
to?: double
```

End of the slide range.

**Type:** double

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
