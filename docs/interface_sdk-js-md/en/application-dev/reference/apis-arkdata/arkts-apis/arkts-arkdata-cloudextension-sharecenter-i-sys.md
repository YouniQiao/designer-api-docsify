# ShareCenter (System API)

Provides APIs for interacting with the sharedCenter service. You need to inherit this class and implement APIs of this class. The system calls these APIs to initiate, cancel, or exit a device-cloud share.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## changeConfirmation

```TypeScript
changeConfirmation(
      userId: number,
      bundleName: string,
      sharingResource: string,
      state: cloudData.sharing.State
    ): Promise<Result<void>>
```

Changes the confirmation state of a share invitation. This API uses a promise to return the result. The application, shared resource ID, and the new conformation state need to be specified. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| bundleName | string | Yes |
| sharingResource | string | Yes |
| state | cloudData.sharing.State | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & lt;void & gt; & gt; |

## changePrivilege

```TypeScript
changePrivilege(
      userId: number,
      bundleName: string,
      sharingResource: string,
      participants: Array<cloudData.sharing.Participant>
    ): Promise<Result<Array<Result<cloudData.sharing.Participant>>>>
```

Changes the privilege (operation permissions) on the shared data. This API uses a promise to return the result. The application, shared resource ID, and the participants with new privilege need to be specified.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| bundleName | string | Yes |
| sharingResource | string | Yes |
| participants | Array & lt;cloudData.sharing.Participant & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & lt;Array & lt;Result & lt;cloudData.sharing.Participant & gt; & gt; & gt; & gt; |

## confirmInvitation

```TypeScript
confirmInvitation(
      userId: number,
      bundleName: string,
      invitationCode: string,
      state: cloudData.sharing.State
    ): Promise<Result<string>>
```

Confirms the invitation for a share. This API uses a promise to return the result. The application, invitation code for the share, and the confirmation state need to be specified.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| bundleName | string | Yes |
| invitationCode | string | Yes |
| state | cloudData.sharing.State | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & lt;string & gt; & gt; |

## exit

```TypeScript
exit(userId: number, bundleName: string, sharingResource: string): Promise<Result<void>>
```

Exits a device-cloud share. This API uses a promise to return the result. The application and shared resource ID need to be specified.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| bundleName | string | Yes |
| sharingResource | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & lt;void & gt; & gt; |

## queryParticipants

```TypeScript
queryParticipants(
      userId: number,
      bundleName: string,
      sharingResource: string
    ): Promise<Result<Array<cloudData.sharing.Participant>>>
```

Queries the participants of a share. This API uses a promise to return the result. The application and shared resource ID need to be specified.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| bundleName | string | Yes |
| sharingResource | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & lt;Array & lt;cloudData.sharing.Participant & gt; & gt; & gt; |

## queryParticipantsByInvitation

```TypeScript
queryParticipantsByInvitation(
      userId: number,
      bundleName: string,
      invitationCode: string
    ): Promise<Result<Array<cloudData.sharing.Participant>>>
```

Queries the participants of a share based on the invitation code. This API uses a promise to return the result. The application and the invitation code of the shared data need to be specified.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| bundleName | string | Yes |
| invitationCode | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & lt;Array & lt;cloudData.sharing.Participant & gt; & gt; & gt; |

## share

```TypeScript
share(
      userId: number,
      bundleName: string,
      sharingResource: string,
      participants: Array<cloudData.sharing.Participant>
    ): Promise<Result<Array<Result<cloudData.sharing.Participant>>>>
```

Shares data. This API uses a promise to return the result. The application that initiates the share, shared resource ID, participants of the share need to be specified.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| bundleName | string | Yes |
| sharingResource | string | Yes |
| participants | Array & lt;cloudData.sharing.Participant & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & lt;Array & lt;Result & lt;cloudData.sharing.Participant & gt; & gt; & gt; & gt; |

## unshare

```TypeScript
unshare(
      userId: number,
      bundleName: string,
      sharingResource: string,
      participants: Array<cloudData.sharing.Participant>
    ): Promise<Result<Array<Result<cloudData.sharing.Participant>>>>
```

Unshares data. This API uses a promise to return the result. The application, shared resource ID, and participants for the data to unshare need to be specified.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| bundleName | string | Yes |
| sharingResource | string | Yes |
| participants | Array & lt;cloudData.sharing.Participant & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & lt;Array & lt;Result & lt;cloudData.sharing.Participant & gt; & gt; & gt; & gt; |
