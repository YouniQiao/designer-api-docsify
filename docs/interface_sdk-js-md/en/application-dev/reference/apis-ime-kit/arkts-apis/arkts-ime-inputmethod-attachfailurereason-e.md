# AttachFailureReason

枚举，绑定失败的原因。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-inputMethod-export enum AttachFailureReason--><!--Device-inputMethod-export enum AttachFailureReason-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## CALLER_NOT_FOCUSED

```TypeScript
CALLER_NOT_FOCUSED = 0
```

表示调用者非焦点窗口所属应用导致的失败。

**使用场景：**应用窗口未获得焦点时调用attach，会返回此失败原因。

**说明：**调用attach前需确保应用窗口已获焦。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AttachFailureReason-CALLER_NOT_FOCUSED = 0--><!--Device-AttachFailureReason-CALLER_NOT_FOCUSED = 0-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## IME_ABNORMAL

```TypeScript
IME_ABNORMAL
```

表示输入法应用异常导致的失败。

**使用场景：**输入法应用进程崩溃或未正常运行时，attach会返回此失败原因。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AttachFailureReason-IME_ABNORMAL--><!--Device-AttachFailureReason-IME_ABNORMAL-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## SERVICE_ABNORMAL

```TypeScript
SERVICE_ABNORMAL
```

表示输入法框架服务异常导致的失败。

**使用场景：**输入法框架服务进程异常时，attach会返回此失败原因。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AttachFailureReason-SERVICE_ABNORMAL--><!--Device-AttachFailureReason-SERVICE_ABNORMAL-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

