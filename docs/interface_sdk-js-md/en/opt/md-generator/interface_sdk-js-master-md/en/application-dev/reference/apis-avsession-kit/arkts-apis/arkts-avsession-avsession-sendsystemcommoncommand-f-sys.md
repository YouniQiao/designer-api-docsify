# sendSystemCommonCommand (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## sendSystemCommonCommand

```TypeScript
function sendSystemCommonCommand(command: string, args: ExtraInfo): Promise<string>
```

Send system control command. The system automatically selects the recipient.

**Since:** 24

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

**Model restriction:** This API can be used only in the stage model.

<!--Device-avSession-function sendSystemCommonCommand(command: string, args: ExtraInfo): Promise<string>--><!--Device-avSession-function sendSystemCommonCommand(command: string, args: ExtraInfo): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | string | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [ExtraInfo](arkts-avsession-avsession-extrainfo-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-session-service-exception) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6600105](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600105-invalid-session-command) |
| [6600107](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600107-too-many-commands-or-events) |
