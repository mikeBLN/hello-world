
class CvLib(object):

    TYPE_OID = 1
    TYPE_STR = 2
    TYPE_SEC = 3
    TYPE_INT = 4
    TYPE_DATE = 5
    TYPE_OCT = 6
    TYPE_ECP = 7

    cvTags = {
        '06':   ['OID', TYPE_OID],
        '42':   ['CAR(issuer)', TYPE_STR],
        '53':   ['discretionary data', TYPE_OCT],
        '5F20': ['CHR(holder)', TYPE_STR],
        '5F24': ['expiration date', TYPE_DATE],
        '5F25': ['effective date', TYPE_DATE],
        '5F29': ['profile indicator', TYPE_INT],
        '5F37': ['signature', TYPE_OCT],
        '65':   ['extensions', TYPE_SEC],
        '7F21': ['CV certifcate', TYPE_SEC],
        '7F49': ['public key template', TYPE_SEC],
        '7F4C': ['CHAT', TYPE_SEC],
        '7F4E': ['certificate body', TYPE_SEC],
        '81':   ['prime modulud p', TYPE_INT],
        '82':   ['first coeff a', TYPE_INT],
        '83':   ['second coeff b', TYPE_INT],
        '84':   ['base point G', TYPE_ECP],
        '85':   ['order of base point r', TYPE_INT],
        '86':   ['public point Y', TYPE_ECP],
        '87':   ['cofactor f', TYPE_INT]
    }

    oIDs = {
        '0.4.0.127.0.7.2.2.2.2.1': 'TA-ECDSA-SHA1',
        '0.4.0.127.0.7.2.2.2.2.2': 'TA-ECDSA-SHA224',
        '0.4.0.127.0.7.2.2.2.2.3': 'TA-ECDSA-SHA256',
        '0.4.0.127.0.7.2.2.2.2.4': 'TA-ECDSA-SHA384',
        '0.4.0.127.0.7.2.2.2.2.5': 'TA-ECDSA-SHA512',
        '0.4.0.127.0.7.3.1.2.1': 'IS-roles',
        '0.4.0.127.0.7.3.1.2.2': 'AT-roles',
        '0.4.0.127.0.7.3.1.2.3': 'ST-roles'
    }

    isRolesMask = 0xC0
    isRightsMask = 0x3F
    atRolesMask = 0xC000000000
    atRightsMask = 0x3FFFFFFFFF
    stRolesMask = 0xC0
    stRightsMask = 0x3F

    isRoles = {
        0xC0: 'CVCA',
        0x80: 'DVCA domestic',
        0x40: 'DVCA foreign',
        0x00: 'Inspection terminal'
    }

    isRights = {
        0x20: 'RFU 5',
        0x10: 'RFU 4',
        0x08: 'RFU 3',
        0x04: 'RFU 2',
        0x02: 'Read DG4 Iris',
        0x01: 'Read DG3 Fingerprints'
    }

    atRoles = {
        0xC000000000: 'CVCA',
        0x8000000000: 'DVCA domestic',
        0x4000000000: 'DVCA foreign',
        0x0000000000: 'Authentication terminal'
    }

    atRights = {
        0x2000000000: 'Write DG17',
        0x1000000000: 'Write DG18',
        0x0800000000: 'Write DG19',
        0x0400000000: 'Write DG20',
        0x0200000000: 'Write DG21',
        0x0100000000: 'RFU 32',
        0x0080000000: 'RFU 31',
        0x0040000000: 'RFU 30',
        0x0020000000: 'RFU 29',
        0x0010000000: 'Read DG21',
        0x0008000000: 'Read DG20',
        0x0004000000: 'Read DG19',
        0x0002000000: 'Read DG18',
        0x0001000000: 'Read DG17',
        0x0000800000: 'Read DG16',
        0x0000400000: 'Read DG15',
        0x0000200000: 'Read DG14',
        0x0000100000: 'Read DG13',
        0x0000080000: 'Read DG12',
        0x0000040000: 'Read DG11',
        0x0000020000: 'Read DG10',
        0x0000010000: 'Read DG9',
        0x0000008000: 'Read DG8',
        0x0000004000: 'Read DG7',
        0x0000002000: 'Read DG6',
        0x0000001000: 'Read DG5',
        0x0000000800: 'Read DG4',
        0x0000000400: 'Read DG3',
        0x0000000200: 'Read DG2',
        0x0000000100: 'Read DG1',
        0x0000000080: 'Install Qualified Certificate',
        0x0000000040: 'Install Certificate',
        0x0000000020: 'PIN Management',
        0x0000000010: 'CAn allowed',
        0x0000000008: 'Privileged Terminal',
        0x0000000004: 'Restricted Identification',
        0x0000000002: 'Community ID Verification',
        0x0000000001: 'Age Verification',
    }

    stRoles = {
        0xC0: 'CVCA',
        0x80: 'DVCA domestic',
        0x40: 'DVCA foreign',
        0x00: 'Signature terminal'
    }

    stRights = {
        0x20: 'RFU 5',
        0x10: 'RFU 4',
        0x08: 'RFU 3',
        0x04: 'RFU 2',
        0x02: 'generate qualified signature',
        0x01: 'generate signature'
    }