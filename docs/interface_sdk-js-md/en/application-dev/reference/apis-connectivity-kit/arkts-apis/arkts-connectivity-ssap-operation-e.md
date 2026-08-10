# Operation

属性操作指示的枚举。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-ssap-enum Operation--><!--Device-ssap-enum Operation-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## READABLE

```TypeScript
READABLE = 0x01
```

当该比特置位后，属性值可被读取。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Operation-READABLE = 0x01--><!--Device-Operation-READABLE = 0x01-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## WRITE_NO_RESPONSE

```TypeScript
WRITE_NO_RESPONSE = 0x02
```

当该比特置位后，属性值可被写入，写入后无反馈。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Operation-WRITE_NO_RESPONSE = 0x02--><!--Device-Operation-WRITE_NO_RESPONSE = 0x02-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## WRITE_WITH_RESPONSE

```TypeScript
WRITE_WITH_RESPONSE = 0x04
```

当该比特置位后，属性值可被写入，写入后产生反馈给客户端。写操作完成后，会反馈给客户端。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Operation-WRITE_WITH_RESPONSE = 0x04--><!--Device-Operation-WRITE_WITH_RESPONSE = 0x04-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## NOTIFY

```TypeScript
NOTIFY = 0x08
```

当该比特置位后，属性值通过通知方式传递给客户端。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Operation-NOTIFY = 0x08--><!--Device-Operation-NOTIFY = 0x08-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

