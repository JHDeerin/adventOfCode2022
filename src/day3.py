"""
Alright - for this challenge, there's a bunch of "items" (ASCII chars, a-z and
A-Z) in "rucksacks" (strings). For each "rucksack", there's exactly 1 item that
appears  in both the 1st/2nd half of each rucksack (so I guess we can assume
all the strings have an even-numbered length?). The goal: find all of these
characters, then get the sum of their values (1-26 for lowercase a-z, 27-52 for
A-Z).

So, basically, find the letter that occurs in both halves of a string, do that
for all the strings, then get the correct value of each letter and sum them up.

Ideas:
-   The value of an "item" can be gotten pretty trivially by checking if the
    letter is uppercase or lowercase (convert it to its numeric ASCII value
    and check the range - or, alternatively, see if char.lower() == char). Then,
    we can just take the letter's ASCII value minus whatever offset is appropriate for the uppercase/lowercase. Should be O(1)
-   For finding the duplicate letter, split the string in half, get the set of
    letters in each half, then take the intersect of the sets - there should be
    exactly 1 item that both halves share.

EDIT: There's a second half to the problem! Here, each group of 3 "rucksacks"
(i.e. strings) is carried by a group of elves, who should share exactly 1
"badge" item in all their rucksacks - i.e. we're doing the same problem, but
finding the 1 item shared between all 3 rucksacks (instead of 2 halves of the
same rucksack).

So, changes required to do this will be to find the shared item between 3 groups
instead of just 2, and to change the group creation logic to be "3 groups of
rucksacks" instead of "2 groups in a single rucksack". Make the intersection
code more generic, and change the grouping. Should be fairly easy.

OUTCOME:
-   Got the first half right with 7763! Wait...that was just the first half?
"""
from typing import List, Set


def get_unique_items(compartment: str) -> Set[str]:
    return set(compartment)


def get_shared_items(item_groups: List[str]) -> str:
    assert len(item_groups) > 1
    unique_item_groups = [get_unique_items(group) for group in item_groups]
    # TODO: Try to get this in a more elegant way?
    shared_items = unique_item_groups[0]
    for group in unique_item_groups:
        shared_items = shared_items.intersection(group)
    return shared_items


def get_misplaced_item(rucksack: str) -> str:
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]

    shared_items = get_shared_items([compartment1, compartment2])
    assert len(shared_items) == 1
    return shared_items.pop()


def item_priority(item: str) -> int:
    assert len(item) == 1
    is_capital_letter = item < "a"
    if is_capital_letter:
        priority = ord(item) - 38
    else:
        priority = ord(item) - 96
    return priority


def get_item_priority_sum(rucksacks: List[str]) -> int:
    misplaced_items = [get_misplaced_item(rucksack) for rucksack in rucksacks]
    return sum(item_priority(item) for item in misplaced_items)


def test_first_example_problem():
    input_rucksacks = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    assert get_item_priority_sum(input_rucksacks) == 157


def test_second_example_problem():
    input_rucksacks = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    assert get_badge_priority_sum(rucksacks) == 70


if __name__ == "__main__":
    test_first_example_problem()

    rucksacks = [
        "WVHGHwddqSsNjsjwqVvdwZRCbcJcZTCcsZbLcJJsCZ",
        "hngprFFhFDFhrDpzzQDhtnBJJRJZbZvTcvbfRCJfBRcBJl",
        "DmptngtFwvvMmwmm",
        "HFddrJnLdqtHBMQBmmVm",
        "gbvNsbhsvQtmZTbQPT",
        "vDshDlczcDhcssscwzQwslLJrSJLpqrrzpnCrSfLSnqq",
        "pDGQDSpFDGzFDQSJqzDhjhQMTjTrwTstbTBTjTtLtbTMBT",
        "zgzVNHHgMwMLbLNB",
        "WRWPgdHCZccggJmJGzJmzGhGCD",
        "sVJNlhldShpdpnnwVnwCwtwggt",
        "WLFFcHWQLPPZQCgtnCgmbtbHwt",
        "MPLWzRMMcGgRrWNDpSSSfDflMlTd",
        "BBMZJcgBRjCZZzBpSvHQvbLvvHCQLQ",
        "VlVTFwDTVGnfWSQPtsDPbvrpDS",
        "wWdqhWlwGVfGwlfTVqFWfWWjzZZBJmMZMNdzZJMpjzNjgJ",
        "FBWFphQBmDmpmMSpDWVcVcvsPcRbrjPMcMsr",
        "HHtdnHnwNCHCTJRTPTzrbvVbcVRr",
        "lHqHwlnlqnGCNGGmWDvvZfpZvG",
        "mfVtmPtsccMmHcHCFfmhVmnpgZLbWPZqWnpqZbZWpgPW",
        "zzvwBrzdQDvpZJfQJZJpLf",
        "BrTBwRdNcfNmfStc",
        "sTlhFLfZTTLcfsLlLDZflvQvRNqRJFNvRMRNvQQRBQ",
        "CWcgwStWwCWWwvgNQvJBvQMQRB",
        "wptGzbzGWVGSCVVlVlLDcVVsfhLTlf",
        "HVnMVGwLLbsGnVsLnwLSBggMhjmgmgmhtmqhtgMhMj",
        "zrZzJRZfzZfrPCrFcWccPdTdHHlvdmlgTghCtmtTgq",
        "NFfcZWWzZrrHLBpBBGVGNG",
        "HqFhhCBCBLmwwCqJCHFvvFdcprrrSSrjRFRjpgrggb",
        "VGzWtQzGGQPVtlVNslVWsPdRpmcRrjpSzcrcbdSmSnSg",
        "WPPGllQMPGmTLvLJBCwM",
        "PvDWRSmTVvSvRhbZRpRpbjjjzM",
        "GBFGHLglHrrrLgGrttbMjpbcpcZJBsBp",
        "lrHgrrndgdNnlHGFQPMMmWPTvvWSCDQn",
        "mmhQShhmhQfzNfTTlShbHJrRtltltJJtHlRLLZ",
        "WscggNqwPWjcGcWWcpNcRJHHprZvZHrvtttZJpJr",
        "jGjgcMGCwPNsGDCcszBfhhQQQDnFnTVVBV",
        "mcGjrwzQcrZtQzZQDZcPssvPVVCPCVLwswwPBC",
        "NJbqHddNSgdPWvvsVHVLPs",
        "NqglNSlJFNSbSNdldNlNdNbTRFDrvRmQrQGtmDrvttQmmtDj",
        "zzcBPnHBjgHjWJvbJQTvScbwcQ",
        "qdspVCFqVqfFqLFCqtpTwtpTbSTbJpwBST",
        "FRLFRCNNqMfdWNmZPBPZrHmm",
        "VmtRRJmtrDrwhRcvPspltvgqtqsd",
        "WGQBZzMMBGBGbZTTWWCMNSgggqnPlsfbqndndccglffg",
        "CWQQZMFWdzMQdJJwJVFrwmmmRw",
        "rZsFfGfNhznzsjhzZfVjGVvVdvSTSJHSDDtcmmmttC",
        "wWpRBWlbWMWlQDvCcRSvJRSStm",
        "LPlwWqbgwqjjcFshNf",
        "lsppsGphmPrRQnvHdRpd",
        "qBgjLqMjgjTLPnzHPrPRLnzv",
        "gSMfNjNtttVbqBbtTSStjTqlhmlZDsDsbWZWFFFsGhlWPm",
        "sPDPDzrGzBsGRsbwrjtSVvthVfQtQw",
        "ClpgFZgNqMWCgqCpMNZqNWmNdtSwtljtVHQhtwfvdHtSdhSj",
        "FpNCJpNcpfCpgNWPGBLcbTGTzTzPnG",
        "mssNLCZqSqmNCHmrqHChJTjTjnRRnnqVnTTGngGTRn",
        "dbwptFwQbvdtcvpZDcDddgzGPjTGgpPTRpzzzgRzTn",
        "BwZdtZldDbrSsNrsrSHl",
        "MLnFWMRWpnpnLnLCmPGTqQsFzBttTQ",
        "SwNlDHNcddglSDBjrqmqGQqqmGtGGwszPP",
        "vdSlNcrvvvnBMbBR",
        "psZPRmTpRpgrlrDRBFgV",
        "jvCqNhwnjhGNqCMqVgFHWtgHBrtwHFrJ",
        "cGvbNcjvvhhjcvbQGcZdZSQpzdpmpPVpdZpd",
        "drTHDdlHzllZDTzTQRQLsPPSsBbSjQdL",
        "MfVVWmNvMnqNmVVpMMgfgMmvBFFfRRLQPPsPfsFLFCFRSFjR",
        "whMnNVnqWmlllHswJTZT",
        "ZSQTTLLlTsbmmDZlmNQSNFfPwHwqCjCCfjwFPwfwLr",
        "MctMJMBVttnhJcBBVctwRHjHRJwJwjFfqPfRwj",
        "vzqgqhBVzzTlZmmTlN",
        "WgvlHJFvljvdBmzcvcwpmchc",
        "TQqZsTZttLZbRZsLLMzzppBmNShCmBNTcNCN",
        "LPMZsMZLMQVgglFPhFHlFl",
        "qsBCPVPqVbwfnMQNmZJnqJgR",
        "hHdrvvLWtvtjWQnZJTMrmpTZgN",
        "DShSShLZdFGPGDPGsPsG",
        "qRBddRzFFqFqHnNnPSnnmmSpgpJm",
        "ssZDQMvvMwppNJWRDRpW",
        "MMvwlsRMcQBjcLqLBBqc",
        "ZGHpwFGvwpHrvfFTMtDfccMjntMntc",
        "RgSCLRLJRSRSQQqJmTDMPMTtsJjnclBjtj",
        "LVmmSSddLCwVHDbzDzZr",
        "psgWdsBjnnJjbZWQDDLNrDcrLVQjLM",
        "zPSCCHqCfqfmWNMcrVSLRM",
        "TPHzWPFTGztqTGgdJdsssvZgwb",
        "gcFgBChcClJjNCPb",
        "sWZdZdrSmWmSZRwSmsvPlsTtTtNMnnlvnJJv",
        "GSWrHZdGQpRrrSGmpWQmQfLfpVzDfghppzBVLBlBqg",
        "BFNqFzBNhqVwmTtsqVst",
        "dMwMwMfCMWbDtDvDssCC",
        "ldMwMSHHMMWJpRpPLLpBzPZjgnZPhN",
        "WczRJhcWggVBdzPPLnCjdvjm",
        "lSpSTpTSsCCmmntNdp",
        "wSFDCTwsGDqQqQVWWcJw",
        "RqPqhDGBhRDrrhBFmPmbgssZbwbgCbwsmZsQ",
        "nCtjMppjfTpjJJfVZwtzZtllLZwLss",
        "MHfpMWdHpSCSfnSTJWhDDFDFBGqDGvvDBDFd",
        "MCCGMCSHVGNTspVWQznddndg",
        "rttLtvRbrhLZrbcQdJnnQdfddsrggf",
        "BbRqltRtHsNNllNC",
        "ncFpcsLLdFmWlRmnllTR",
        "bMMVzVqMzjNVDblmRTPGlSmmPlqG",
        "gNDDJMVZNCbNJNDNQCbZCbscvBsdBvrRHfcpdQpfFFff",
        "VnWFbZvFbHWhFjZWVJZJLZFWTttpMCspQTTzQCHpgQMgztzT",
        "dGcfdNdGrlRlBDGNSllfBMspgzmTgtQQgztMtzpmcT",
        "lBNdqRsBRdfPNrLPFVVPVJPZZvhj",
        "TLWgggJzwjgWgjgGnnmQnzQfNNNQsm",
        "SpPbBlPBMlvFZpbbBmQGsmCJmCstsdNGBQ",
        "MhSHhZPrPbvSFrJPpPMSbMcLjjqTLHDRTDDTTLDLTqgH",
        "fprRRbbznFbcQVPDdQPdFV",
        "LTvmsLmcsHmvDvSZDZVVSS",
        "jWtmLccssJTLjHmLWWJwnwlBfwnBbllpCBnffbBr",
        "plPBWzbnFLPPtGqMMwlMGwmS",
        "ZQjDHjrQjdjVFwdMvCSfmwMqdt",
        "DDhhrRDjQghHJjhWBbgbTccbsTzpWF",
        "vgCbbwsTbWWWgwBWDGGDqtPGtMgGlFMH",
        "znrznJNhLSLphRRRDlFPMmpFPjjHtMFF",
        "llNcSQVSNcRbvCwwWcTdwZ",
        "qpnJbnRRnJhRFhFHRgQSzHlSRHCCCg",
        "fMBttBvsBjffvsQTtfGTWlCWsSgSmHCzZmLlHgzZ",
        "ffMdjrfdwjfwwnhJPFchhqwQ",
        "NCVSTCVCQCCRVDQSJsqFPsPNspFhhsgjPh",
        "btvtWtcWnpgmFhjmmt",
        "cfnffBfcWcrMdbvMQJDDrDTDVCpCDrGD",
        "fZNhBWFSlFQFjWQTTldHgCwvTvqqdr",
        "zznVzCznmHvnwgdH",
        "PMMbCGPMDPcLbJhFhWhBhRScQZBQ",
        "WQMrDWGHbSWHMNrTQRhghmgPZccmqDLwPqPg",
        "svCzfpdzzdsnslCsnPZcHZPlJcqZgmqPPc",
        "nntVpdpVsfjCHzvnsCzRTBrtWGbNNQSMbTNSRr",
        "SnpDQdBqGpDSBMfQGcMQBDJPNstvJcWNsPJCtJtNRWPC",
        "VrVHrhTHlPHTvvNtbhNRNswC",
        "TzlFHHmrVlgTlTGSzGqpdMGBPQBS",
        "zrCDnrDVCnCgnrHgGDnVVCZsNttQZmjtsmbMqGqsjbqj",
        "TlRRWPSwwFwbSwTTTpNQQqNjqZZlmMMQQt",
        "wvbwbRTLWdFFwvRBTbvTTRzrnznnJrDDCzBczBfHCJnz",
        "SvTdmLNNNdvTBmvmLvSvDpgczzjfgjggpcjcNPzD",
        "VJHQsJVlHpjjpzsjzP",
        "VRlJbJQrVbVHJJPMhBdnBRCSLZZZnvnLvv",
        "tMGcpGtMtLtsCGspLzNCBBmwCzQRzBBRWQ",
        "hdlHFllDdZgDbDDlDHTWWTnzBBBvzmNHzwRz",
        "FSddDlFRqDFqFSdPVqdhcfGMsVtVfLjrfGfjtMcs",
        "RGMWnBMWfCCMBHTDptJJgZStRPmSRD",
        "bqzFqjqcFLNLZZSmpSBgZZ",
        "rFrQNbNBlNcbrQlNQvvclMswTCTCnwrwHrWGsGCswn",
        "WLhJQddCQwRNCQNHczHNzMvZcZvcNc",
        "SlSpSlrpDqnbqDjlGjGGljTjMZZPPMMfVPgfHMMVgVvqfgcw",
        "SbGsDspbbnjTjBldCFmLwFCJLBmtJB",
        "TMDjMvMqMvDTzcmFCgrJCr",
        "ZZZJSZWVBHZWSSZQJhVhWnHJwczGGwGcCCFzwgmzcwFgwVzc",
        "pLHNQSnNJsMLRJds",
        "TsLZGwdsDFWHBZJFfZ",
        "mqhRvqrzJRbmzJBFfgHHgWgHrrlH",
        "JvvNhJmvtDdsNTwdLV",
        "wwnSVSmwtbstznwgbzzVMTNpTNWdlCSlSWTffWNCSN",
        "cFvccLGFGvvGHZflnNTpnZpZcB",
        "GPqGDhGGqrDhVRgbnbttPmgs",
        "rzSZJScLrcBLvjvsqMPZvjQl",
        "nnpDqgDqFTgwqHHvMHvvvTvPMM",
        "GnqCGpDqqVhccLmrmSmCRL",
        "tJSTmdfddDTDJCPmbQvQLHvqqqbrbvlP",
        "zWGsjcwwGGcVVjcGWcNjvNjQqrQtNFFQHHrF",
        "RZnRVsswRsGWcwVBZVtBRdDJgCffTgmgfnnCpfTfTM",
        "FnCrzhTrNPrMcnhMTnZZZNPwDPdbDmdDtwjdtjbmQwDt",
        "sBvWrpppvLBsLRVBfHSfbbQmbwSjStDSwSwS",
        "LVRRRJqqlHNlNTChrhMG",
        "WNsfsstMvtMvNNGPZwmZmqZPLWZcww",
        "rDCdDRCDFQjSVLcmZcDq",
        "bBBHqTgBbQlQRCQFbgqdhvshGvTJMnfTtnnThnsN",
        "VwWBTNQcVzDtrgfrtzzt",
        "LLbpShLGvlbCmLjpGSCSCpvFdrgdddcHtrtGgfqHcDHqrd",
        "pmvLmlpmjbLbpljJPBBcTBBQRZBBVJRZ",
        "cVTcVTNvvghNhvggPPgtCVSpSQmzCqZDRCmDZDZS",
        "dGJMWFsFMFWsnlzRlQzlzqpzlZzD",
        "HdLFssFMsJbnbFjqbhPgjNggcrhg",
        "LLVhQCTvRvmWlCppQfQQjPrwszNsfzNz",
        "BZSgncHgnJStJHJgntMWzGsrPqGwsfPfGPwwwZ",
        "bdBdJMBcShWCLbhWVC",
        "vjdpGNGwSNCTwwRbfnWgQMLjQWMnLQ",
        "DcmFPFtHmlcgpqWDnMbDLf",
        "FZJPtcprHtPPHplZHPZclwwGBSZSvSwCwvZzNdwvvw",
        "CdJLJCJPWPWcbtzJtqJzFrQvBhfjBBvjjvdjpFjr",
        "sBRgsZGDNSBBRGDwphrrrThpHpgHvhpQ",
        "DwDsGBDNwGmMNlMlMDSPmztJVCbVCCWqPqJLmW",
        "LSTMgDSRSMHbMDWLHSvDScwtCGqGrjGrcLftqVGtVC",
        "hzJPmlphCGrCwVrJ",
        "zhPNdNnQZBZBhZnNZSgMWMDbMHwWSDWNDH",
        "rcdvvcwvrHrMZBjHSZ",
        "sDtWblgnltsDFlgFqltCCVQTMTgSHVTfSQfSHj",
        "tDtRWFpFbWWWWNNDWsNqWvmzvhzhzGmzjjGvLwJmpc",
        "nFSSnnbhSfgLSSnVjdjfHMgfMzGzmqlNGGmTPlqqTzTNNzlT",
        "pBZsJJvccbBmlWGlNb",
        "cvsssvZwsDwrDdfFgnbDfVbgng",
        "mWRNWNCTdwdCwhCddbWWmhsZVgJQJBVBfsBsJQLQBLJb",
        "qFFlGzFtjjcqzHtFtlRfVfsZfQHVfBHQRHgf",
        "jqGjtcDnGnPzFRlzrnMdWrrCMMddNNWT",
        "MHWCjjGMcHhbhPDLphHQ",
        "nRVJrtgssdLgCppvLQbg",
        "RlVVZNVRJlsstldsBCNlczfjjSZmWTcmGmTSfmSm",
        "RTHqgTgMwgnGTRzqTHCGfdFdfhmBrJrdvbFJMhPB",
        "lNZNNNLttLWJBPBdZBFmdZ",
        "SppscpLVStclNPWtCczqnQQwHTTgCGwq",
        "hSHRCbZRSZhbRZBctnMVjwwtWtwh",
        "GrdFzQrDdJstjcWttwsF",
        "drPJLDPGPvDvzrJPQLdDHpZlwLgRmwCHLpwgSbff",
        "zMSSnCtCdSdCtdfMdHMdtVBDjhWDHBqbTVVBqhbDjr",
        "cPNhFFNRlNDlTBqjlTBG",
        "RvmvRpPNRgwgPvFwhmdCssmCzdMshMmL",
        "tttjgrpTwmCgCwgwrrlrHzbzqqFNzdJqqZnddJwNbh",
        "cQjMjPMBfcLBSjGQBndFnzNdNnhzzNGFbF",
        "sSQPLMfVPBVSfBMvVLSPfHCttDjCDRRtrVVglgpttD",
        "vdTvdpBvcTPdSSvCLrCCDLDCQGDl",
        "sRfnFgmFRMVsnqgRmqzmrrDBDwtHlLHtrLCDGL",
        "qRMVjJgRFnJfMssMsgZScPJpZbPbPPWhBZSp",
        "ZJgNJhGZglMZZFDTPSNqFSqTSb",
        "mwdvwpsjrcjBvpwFrvbHcDqbWHRWDSPWDHSR",
        "CsvpsLLjFzhlLGFZ",
        "sDNQrMrNfrlQjJRgGjbTllHG",
        "ZRhSnWFVSwBtFRBVvVgHgbzjgGTJnngmGmHC",
        "vWZLShhvZLVtSFSLqwVrQdqpcqMDddRNQMdsNP",
        "hQhSQbbwtHzShwhSQPbJRsLwRCjJmDCcvmqCcs",
        "FNdBTBTNMsRqqCjTjL",
        "GNdrdMBVFShhSLSGGL",
        "cZzcCmjjcvdzdWqgWTZgPZgZhh",
        "wSwVGSJFTffgJTNh",
        "FSVpVlBMShzbjzcpvp",
        "qqlblClRbnTvqTmRqlmnTwrdfdwFFNrngfddDBrNtr",
        "PcLcQLMVLGMzHLMchhLcjLFrrNrBfrfFNJtNgJDDBNzt",
        "sSjjGcGQscSVSMjHVMSVPSQsWmCmppZCmtCWbbWTlZTqTl",
        "qWlVJmDJHWJHVJlsdVTdhbFNNgFhwhhhFhwwZg",
        "npjnvQpStCQLvBpPnvtBtBpGSGbzbGDggGNbgwghzZNGGN",
        "jBvLtvjnrtMDmmDRTTrsWc",
        "pmwdwzJtFmmlpFsWwtstJPGgvNgCCLWCvPgNNPQCQv",
        "RfbfTRBnRGQvPNnncc",
        "ZTbPZSDSBfSBVSbbBRbbbtrFdtlFmVsswtFwzdpszw",
        "hVphQcmdcWWprWWhChFQBsfHjDTTBCHlSsTSBgSH",
        "vqBRqqzbqMZPMwSTDjJjlHDllgHZ",
        "PMnMLqtMnntQhWBccthB",
        "vqqvCSvHSSwqvqCddnvQFmNbVjbJVVmGNNVHNNlH",
        "pggrhzWgptWhZsmVlFmgNNVNbj",
        "RzpMLLhhphtzrRrSSbQTBQwSTDBwQM",
        "DSFQDlDFRddDHQHQtFlDVsVMTzrMCLSWZLZffSzLWrfCJz",
        "jjBBvpgmbppBPbMwBBBNbbZWZzzCCTzzZgzWcJccLzWz",
        "bvPwNwmpnBNhPmqpPvnwwNmtRQGQMdQDQlsGVVGhRlGFsl",
        "SfJJwDJgpGdSGJNSTwTVJDRbWWfLtCWCLtRLHWrtbWBf",
        "cQQPnFhjjQlczhqllhszhqsQRWnrbrHdHtbWrBWBbtvvHBrW",
        "qMqqqqzFFmPjmmsFjmzsmhjcDGSZTJgTdpZwZgwSZVpMTNVG",
        "czrcHMcMJtCCPnpFmH",
        "DwGGlvLljGmDRdwLdLjfhtFsssnFVpfttpptsnFPnp",
        "TlRTghTjwTDRTDlZZQgWMMrMJMSZmM",
        "BzdNzNdgNNPfgdNsdQdNvVMLLVQVMcCRCMRmvCGc",
        "zHpplwwZrZlqlWWrpZwqlHhLvqMCRDCGVmLcqGMVvCMmMD",
        "rWrjwWwHplZbwpZtHtJJbgfFTfsNnBbsfbSdTzgB",
        "jPRRppDLDGDTLLggMMjpLTGcrJWHsttJfwnWrMvrJnvnrNfJ",
        "blqbzBdzmhhbQWnsNHtJvfssfd",
        "lhFhzSzzSZVNSlVPgDPCPCGTRcGR",
        "cqWcNWffPftvsvfpqPtZsBzrbmbFddBmbcLbdDHbHz",
        "TJgljTnGgnLBTZbHdBFz",
        "JgSnJwSlgGJRwMtfPtvfwsZQZZtv",
        "hHhPbQPTwsdwdHqtgttjpNfjDt",
        "FFlCmSzRCCmlzzRGCFNvRpvjvtZNZqsRfNRg",
        "mVmsFMGFzJFBwQTMnMQndd",
        "QQVpQGcVdGmspHHLtbqfqfbt",
        "JvZTFDFzJzhFCWCZZDzWPBCJfLbnnwLqttnsHHNPwtbHLwjn",
        "DssTMWvvvGMcQGQGld",
        "sshRHZSZRbSZHhBFBMpMWpFgbbtb",
        "JfjTjmwwTPvfTNPTQlmFFFqqmFMBBqFgFt",
        "vDTvJffQTJjJvPvTNSHRzhCsShRRRDtZHz",
        "NFLsRDNNDNBDlgPPgBglQlzj",
        "HJhdZpfJzlWQjjHw",
        "ffJTppZZqTNlGnNsMG",
        "ZMrWcWwqqvPZMndGdqlnnDLnVT",
        "HpCsshCfpFfHHJDDSlSVQQGGflDQ",
        "zssNzRJFhjNHNNHpJRwbwMMzWWtZPcbBbwbG",
        "HlNHHLHsBDRpHLlsHRlJnMhfWZMRnvCCCnWhZj",
        "wtqSmQqttzSSQdPmmwZhChJjWJjPggCZCfZJ",
        "SSwtTbTQmbtdqmGTTcfqzDLHFsBLDGLNGrsBHFGrLB",
        "FFDvWznMWWMrPnPnWPgsmgQbhJRslHbwHwVVsVHjBsHb",
        "ZtSffffpdLqpSCLfCNqfLqLCjHjHbwhpBwJllHlRVQllphjj",
        "ZcNCtcGSctZScqfNGScLNcczPJFmzmDzGzWnrWFPFWDvrM",
        "DnTPspmTPsTCDQWRZzZzZRCRfCfHfh",
        "BNcqTBcFgbVchVJhVR",
        "dTwdrBrwTSPPWnnmSmsn",
        "pfbbDbHpNBFmQbpNNBSlLtlDStSdSPJLtLJR",
        "ZcszvwgVCZswFzVTRTlTlRLgRJSWJR",
        "jzZvVwFjcjjnwvzwZcjMpqMpbGQbQmhhHhmfHQmh",
        "hTbddhQCtdNmdtwtdhTBbCddRSWscczwcRSWLJzcFJzDsFsR",
        "NflgfPZPcgSLJcWD",
        "lPVNZMMMpZlZZvfrMvpbQHQhtbtqdTQHthrqhd",
        "JlWSStwhWJSRJpJvJBjTwTqcwTsDjsCTCB",
        "dqFzgFZGGQNVmTcCrjrzsBrB",
        "fdgLFQLnPdnqShRMPhlJMpWW",
        "TMPcsPDjdDhsDcDcTTTDvdvghBNFGGtmNrSrgSSBGNtNFg",
        "CVCbJqlRVVWWpRqRQZRWVWJZBtmSFGNmggGmtmmBFbrGMGMt",
        "JRqHVJVCRLZWTjMnfLTPcfLd",
        "TRTZFTTrghrZVhVWdWZpMmbzbdzBmtDpDDzmzB",
        "wcsSSsjfPfGPqQwqsQcfJJCtJGpppCBJzCbzJzCb",
        "sPjflcwljfjfvqNcTZTRhtVWrNrVLnrR",
        "rVLLsmwmCWTmsCTdwQrdTmqWDjDHjNGNPbjDBPNDNsZRDBjH",
        "cFcSvgJvfhfLnShtMJtPHRRvRbBBGBPNBHPbND",
        "hgLcgcLpJSMwzmrmzqQrmp",
    ]
    priority_sum = get_item_priority_sum(rucksacks)
    assert priority_sum == 7763
    print(priority_sum)
