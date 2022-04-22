import pickle

with open("model.h", "rb") as file:
    model = pickle.load(file)
keys = [
    "ls3",
    "soct2",
    "idio2",
    "it1",
    "l1b",
    "aoj11",
    "b1",
    "b2",
    "b3",
    "b4",
    "b6",
    "b43",
    "b12",
    "b13",
    "b18",
    "b21",
    "b32",
    "b37",
    "b47a",
    "m1",
    "m2",
    "infrax",
    "infra3",
    "ros1",
    "ros4",
    "ing4",
    "eff1",
    "eff2",
    "aoj22new",
    "media3",
    "media4",
    "pn4",
    "d1",
    "d2",
    "d3",
    "d4",
    "d5",
    "d6",
    "lib1",
    "lib2b",
    "lib2c",
    "lib4",
    "usmex1",
    "exc7new",
    "pol1",
    "q5a",
    "q5b",
    "q10new",
    "q12bn",
    "q12",
    "www1",
    "gi0",
    "a4_10",
    "a4_11",
    "a4_12",
    "a4_13",
    "a4_14",
    "a4_15",
    "a4_16",
    "a4_17",
    "a4_18",
    "a4_19",
    "a4_2",
    "a4_20",
    "a4_21",
    "a4_22",
    "a4_25",
    "a4_26",
    "a4_27",
    "a4_3",
    "a4_30",
    "a4_31",
    "a4_32",
    "a4_33",
    "a4_4",
    "a4_5",
    "a4_55",
    "a4_56",
    "a4_57",
    "a4_58",
    "a4_59",
    "a4_6",
    "a4_61",
    "a4_70",
    "a4_9",
    "np1_2.0",
    "prot3_2.0",
    "vic1ext_2.0",
    "vb1_2.0",
    "vb1_3.0",
    "vb2_2.0",
    "usvb1011_4002.0",
    "usvb1011_4003.0",
    "usvb1011_77.0",
    "usvb20_2.0",
    "usvb20_3.0",
    "usvb20_4.0",
    "usvb20_5.0",
    "aca6_2.0",
    "aca6_3.0",
    "aca6_4.0",
    "aca6_5.0",
    "aca6_6.0",
    "aca6_7.0",
    "aca6_8.0",
    "q3c_10.0",
    "q3c_11.0",
    "q3c_12.0",
    "q3c_2.0",
    "q3c_3.0",
    "q3c_4.0",
    "q3c_5.0",
    "q3c_6.0",
    "q3c_7.0",
    "q3c_77.0",
    "q11n_2.0",
    "q11n_3.0",
    "q11n_4.0",
    "q11n_5.0",
    "q11n_6.0",
    "q11n_7.0",
    "etid_4.0",
    "etid_4003.0",
    "etid_4004.0",
    "etid_4005.0",
    "etid_4006.0",
    "etid_4008.0",
    "etid_7.0",
]
result_mapping = {
    0: "Blank Ballot",
    1: "Null Ballot",
    2: "Democrat (Hillary Clinton)",
    3: "Republican (Donald Trump)",
    4: "Libertarian (Gary Johnson)",
    5: "Green Party (Jill Stein)",
    6: "other parties",
}

most_common_output = {
    "ls3": 2,
    "soct2": 2,
    "idio2": 2,
    "it1": 2,
    "l1b": 5,
    "aoj11": 2,
    "b1": 5,
    "b2": 4,
    "b3": 4,
    "b4": 5,
    "b6": 5,
    "b43": 7,
    "b12": 7,
    "b13": 1,
    "b18": 6,
    "b21": 1,
    "b32": 5,
    "b37": 1,
    "b47a": 6,
    "m1": 5,
    "m2": 4,
    "infrax": 1,
    "infra3": 2,
    "ros1": 1,
    "ros4": 1,
    "ing4": 7,
    "eff1": 1,
    "eff2": 6,
    "aoj22new": 7,
    "media3": 1,
    "media4": 7,
    "pn4": 2,
    "d1": 10,
    "d2": 10,
    "d3": 10,
    "d4": 10,
    "d5": 10,
    "d6": 10,
    "lib1": 2,
    "lib2b": 2,
    "lib2c": 2,
    "lib4": 2,
    "usmex1": 3,
    "exc7new": 4,
    "pol1": 1,
    "q5a": 5,
    "q5b": 1,
    "q10new": 8,
    "q12bn": 0,
    "q12": 0,
    "www1": 1,
    "gi0": 1,
    "a4_10": 0,
    "a4_11": 0,
    "a4_12": 0,
    "a4_13": 0,
    "a4_14": 0,
    "a4_15": 0,
    "a4_16": 0,
    "a4_17": 0,
    "a4_18": 0,
    "a4_19": 0,
    "a4_2": 0,
    "a4_20": 0,
    "a4_21": 0,
    "a4_22": 0,
    "a4_25": 0,
    "a4_26": 0,
    "a4_27": 0,
    "a4_3": 0,
    "a4_30": 0,
    "a4_31": 0,
    "a4_32": 0,
    "a4_33": 0,
    "a4_4": 0,
    "a4_5": 0,
    "a4_55": 0,
    "a4_56": 0,
    "a4_57": 0,
    "a4_58": 0,
    "a4_59": 0,
    "a4_6": 0,
    "a4_61": 0,
    "a4_70": 0,
    "a4_9": 0,
    "np1_2.0": 1,
    "prot3_2.0": 1,
    "vic1ext_2.0": 1,
    "vb1_2.0": 0,
    "vb1_3.0": 0,
    "vb2_2.0": 0,
    "usvb1011_4002.0": 0,
    "usvb1011_4003.0": 0,
    "usvb1011_77.0": 0,
    "usvb20_2.0": 0,
    "usvb20_3.0": 0,
    "usvb20_4.0": 0,
    "usvb20_5.0": 0,
    "aca6_2.0": 0,
    "aca6_3.0": 0,
    "aca6_4.0": 0,
    "aca6_5.0": 0,
    "aca6_6.0": 0,
    "aca6_7.0": 0,
    "aca6_8.0": 0,
    "q3c_10.0": 0,
    "q3c_11.0": 0,
    "q3c_12.0": 0,
    "q3c_2.0": 0,
    "q3c_3.0": 0,
    "q3c_4.0": 0,
    "q3c_5.0": 0,
    "q3c_6.0": 0,
    "q3c_7.0": 0,
    "q3c_77.0": 0,
    "q11n_2.0": 0,
    "q11n_3.0": 0,
    "q11n_4.0": 0,
    "q11n_5.0": 0,
    "q11n_6.0": 0,
    "q11n_7.0": 0,
    "etid_4.0": 0,
    "etid_4003.0": 0,
    "etid_4004.0": 0,
    "etid_4005.0": 0,
    "etid_4006.0": 0,
    "etid_4008.0": 0,
    "etid_7.0": 0,
}
