# OutputType

Enumerates output type of hilog.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-hilog-enum OutputType--><!--Device-hilog-enum OutputType-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

## DEFAULT

```TypeScript
DEFAULT = 0
```

DEFAULT Default output type, equivalent to CONSOLE\_ONLY.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OutputType-DEFAULT = 0--><!--Device-OutputType-DEFAULT = 0-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

## CONSOLE_ONLY

```TypeScript
CONSOLE_ONLY = 0
```

CONSOLE\_ONLY Hilog is output to the console only, equivalent to DEFAULT.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OutputType-CONSOLE_ONLY = 0--><!--Device-OutputType-CONSOLE_ONLY = 0-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

## PRIVATE_SANDBOX_ONLY

```TypeScript
PRIVATE_SANDBOX_ONLY = 1
```

PRIVATE\_SANDBOX\_ONLY Hilog is output to files in its own private sandbox.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OutputType-PRIVATE_SANDBOX_ONLY = 1--><!--Device-OutputType-PRIVATE_SANDBOX_ONLY = 1-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

## SHARE_SANDBOX_ONLY

```TypeScript
SHARE_SANDBOX_ONLY = 2
```

SHARE\_SANDBOX\_ONLY Hilog is output to files in its own sandbox, accessible to itself and the hiview service.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OutputType-SHARE_SANDBOX_ONLY = 2--><!--Device-OutputType-SHARE_SANDBOX_ONLY = 2-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

## PRIVATE_SANDBOX_WITH_CONSOLE

```TypeScript
PRIVATE_SANDBOX_WITH_CONSOLE = 3
```

PRIVATE\_SANDBOX\_WITH\_CONSOLE Enable both CONSOLE\_ONLY and PRIVATE\_SANDBOX\_ONLY at the same time.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OutputType-PRIVATE_SANDBOX_WITH_CONSOLE = 3--><!--Device-OutputType-PRIVATE_SANDBOX_WITH_CONSOLE = 3-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

## SHARE_SANDBOX_WITH_CONSOLE

```TypeScript
SHARE_SANDBOX_WITH_CONSOLE = 4
```

SHARE\_SANDBOX\_WITH\_CONSOLE Enable both CONSOLE\_ONLY and SHARE\_SANGBOX\_ONLY at the same time.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OutputType-SHARE_SANDBOX_WITH_CONSOLE = 4--><!--Device-OutputType-SHARE_SANDBOX_WITH_CONSOLE = 4-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

