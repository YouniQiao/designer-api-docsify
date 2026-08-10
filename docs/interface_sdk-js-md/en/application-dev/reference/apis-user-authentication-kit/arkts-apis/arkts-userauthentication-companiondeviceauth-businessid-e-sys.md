# BusinessId (System API)

业务ID枚举。业务ID是伴随设备支持的某个业务场景的唯一标识。不同的伴随设备由于认证安全性差异，支持的业务场景范围也不同，例如免解锁执行语音指令。

不同业务ID的伴随设备关系是独立的，互不干扰，可以独立添加、删除、认证。

当前伴随设备模块的业务包括锁屏解锁、解锁应用锁、语音指令在锁屏执行前的身份鉴权等业务场景。

业务的添加对于服务端设备支持的场景有要求，如多屏协同业务，要求服务端设备支持委托认证场景。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-companionDeviceAuth-enum BusinessId--><!--Device-companionDeviceAuth-enum BusinessId-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

## DEFAULT

```TypeScript
DEFAULT = 0
```

默认业务ID。系统预设的默认业务，用于基本的伴随设备认证场景。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BusinessId-DEFAULT = 0--><!--Device-BusinessId-DEFAULT = 0-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

## VENDOR_BEGIN

```TypeScript
VENDOR_BEGIN = 10000
```

厂商自定义业务ID取值起点。厂商可在此值基础上自定义扩展业务ID，实际取值需大于等于10000，避免与系统保留值[0-9999]冲突。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BusinessId-VENDOR_BEGIN = 10000--><!--Device-BusinessId-VENDOR_BEGIN = 10000-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

