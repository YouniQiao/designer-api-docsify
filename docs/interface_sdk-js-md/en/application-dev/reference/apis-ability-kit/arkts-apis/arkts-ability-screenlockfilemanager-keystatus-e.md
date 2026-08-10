# KeyStatus

表示锁屏下敏感数据密钥状态的枚举。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-screenLockFileManager-export enum KeyStatus--><!--Device-screenLockFileManager-export enum KeyStatus-End-->

**System capability:** SystemCapability.Security.ScreenLockFileManager

## KEY_NOT_EXIST

```TypeScript
KEY_NOT_EXIST = -2
```

密钥不存在。此状态表示应用未开启锁屏下敏感数据保护功能，或当前设备上该保护功能不可用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-KeyStatus-KEY_NOT_EXIST = -2--><!--Device-KeyStatus-KEY_NOT_EXIST = -2-End-->

**System capability:** SystemCapability.Security.ScreenLockFileManager

## KEY_RELEASED

```TypeScript
KEY_RELEASED = -1
```

密钥已释放。此状态表示锁屏下敏感数据无法被操作。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-KeyStatus-KEY_RELEASED = -1--><!--Device-KeyStatus-KEY_RELEASED = -1-End-->

**System capability:** SystemCapability.Security.ScreenLockFileManager

## KEY_EXIST

```TypeScript
KEY_EXIST = 0
```

密钥存在。此状态表示锁屏下敏感数据可以被正常操作。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-KeyStatus-KEY_EXIST = 0--><!--Device-KeyStatus-KEY_EXIST = 0-End-->

**System capability:** SystemCapability.Security.ScreenLockFileManager

